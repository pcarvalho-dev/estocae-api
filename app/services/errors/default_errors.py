from app.services.errors.exceptions import NotFoundError, BadRequestError, ConflictError

treated_errors = (ConflictError, NotFoundError, BadRequestError)
