from datetime import datetime
from flask import current_app
from flask_sqlalchemy import SQLAlchemy, Model, get_state
from sqlalchemy import orm
from functools import partial


class CRUDMixin(Model):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """
        It takes a class and returns a function that takes keyword arguments and returns an instance of the
        class
        
        :param cls: The class that the method is being called on
        :return: The instance of the class.
        """
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """
        It takes a dictionary of attributes and values, and updates the model instance with those values
        
        :param commit: If True, then the changes are saved to the database. If False, then they're not,
        defaults to True (optional)
        :return: The object itself.
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """
        It adds the object to the database, and if the commit parameter is True, it commits the changes to
        the database
        
        :param commit: If True, the changes will be committed to the database. If False, the changes will be
        saved in the session, but not committed to the database until you call db.session.commit(), defaults
        to True (optional)
        :return: The object itself.
        """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """
        If the commit parameter is True, then set the deleted_at column to the current time and commit the
        changes to the database
        
        :param commit: If True, the object will be committed to the database. If False, the object will not
        be committed to the database, defaults to True (optional)
        :return: The return value is the result of the expression.
        """
        self.deleted_at = datetime.now()
        return commit and db.session.commit()

    def delete_real(self, commit=True):
        """
        It deletes the object from the database, and if the commit parameter is True, it commits the change
        to the database
        
        :param commit: If True, the session will be committed after the object is deleted, defaults to True
        (optional)
        :return: The commit and db.session.commit()
        """
        db.session.delete(self)
        return commit and db.session.commit()


# ROUTING DB
class RoutingSession(orm.Session):
    def __init__(self, db, autocommit=False, autoflush=False, **options):
        """
        The function creates a new session object, and binds it to the database engine.
        
        :param db: The SQLAlchemy database object
        :param autocommit: If set to True, all objects will be automatically committed after each flush,
        defaults to False (optional)
        :param autoflush: If set to True, all queries will be automatically flushed prior to their
        execution. This is a shortcut to calling flush() explicitly, defaults to False (optional)
        """
        self.app = db.get_app()
        self.db = db
        self._bind_name = None
        orm.Session.__init__(
            self, autocommit=autocommit, autoflush=autoflush,
            bind=db.engine,
            binds=db.get_binds(self.app),
            **options,
        )

    def get_bind(self, mapper=None, clause=None):
        """
        If you have a bind name, use it. Otherwise, use the default
        
        :param mapper: The mapper associated with the query
        :param clause: The SQL expression being compiled
        :return: The return value is a SQLAlchemy engine object.
        """
    
        try:
            state = get_state(self.app)
        except (AssertionError, AttributeError, TypeError) as err:
            current_app.logger.info(
                'cant get configuration. default bind. Error:' + err)
            return orm.Session.get_bind(self, mapper, clause)

        # If there are no binds configured, use default SQLALCHEMY_DATABASE_URI
        if not state or not self.app.config['SQLALCHEMY_BINDS']:
            return orm.Session.get_bind(self, mapper, clause)

        # if want to user exact bind
        if self._bind_name:
            # current_app.logger.info("Connecting -> SLAVE")
            return state.db.get_engine(self.app, bind=self._bind_name)
        else:
            # if no bind is used connect to default
            # current_app.logger.info("Connecting -> DEFAULT")
            return orm.Session.get_bind(self, mapper, clause)

    def using_bind(self, name):
        """
        It creates a new session object, copies all the attributes from the current session object to the
        new session object, and then sets the new session object's bind name to the name passed in
        
        :param name: The name of the database to bind to
        :return: A new RoutingSession object with the same attributes as the original RoutingSession object.
        """
        bind_session = RoutingSession(self.db)
        vars(bind_session).update(vars(self))
        bind_session._bind_name = name
        return bind_session


class RouteSQLAlchemy(SQLAlchemy):
    def __init__(self, *args, **kwargs):
        """
        It allows you to use the `using_bind` method on the session object, which is a method that is not
        normally available on the session object
        """
        SQLAlchemy.__init__(self, *args, **kwargs)
        self.session.using_bind = lambda s: self.session().using_bind(s)

    def create_scoped_session(self, options=None):
        """
        It creates a new session object and binds it to the database engine.
        
        :param options: A dictionary of keyword arguments that will then be sent to the sessionmaker
        callable used to create the session
        :return: A new session object, bound to the database engine.
        """
# Creating a new session object, and binding it to the database engine.
        if options is None:
            options = {}
        scopefunc = options.pop('scopefunc', None)
        return orm.scoped_session(
            partial(RoutingSession, self, **options),
            scopefunc=scopefunc,
        )


# Creating a new RouteSQLAlchemy object, and passing in the CRUDMixin class as the model_class
# parameter.
db = RouteSQLAlchemy(model_class=CRUDMixin)
