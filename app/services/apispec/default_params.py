class DefaultParameters:
    def __init__(self, spec):
        self.spec = spec
        self.data_path_params = {"name": "item_id",
                                 "type": "integer",
                                 "description": "ID to return"}

        self.page_params = {"name": "page",
                            "schema": {"type": "integer"},
                            "description": "Number of the page"}

        self.per_page_params = {"name": "per_page",
                                "schema": {"type": "integer"},
                                "description": "The numbers of items to return"}

        self.search_params = {"name": "search",
                              "schema": {"type": "string"},
                              "description": "Search parameter by name"}

        self.order_required_params = {"name": "order",
                                      "schema": {"type": "string", "required": True},
                                      "description": "Sort column"}

        self.order_by_required_params = {"name": "order_by",
                                         "schema": {"type": "string", "required": True},
                                         "description": "Sorting type"}

    def __path_params_default(self):
        self.spec.components.parameter(component_id="path_params_default",
                                       location="path",
                                       component=self.data_path_params)

    def __page_params(self):
        self.spec.components.parameter(component_id="page_param",
                                       location="query",
                                       component=self.page_params)

    def __per_page_params(self):
        self.spec.components.parameter(component_id="per_page_param",
                                       location="query",
                                       component=self.per_page_params)

    def __search_params(self):
        self.spec.components.parameter(component_id="search_param",
                                       location="query",
                                       component=self.search_params)

    def __order_required_params(self):
        self.spec.components.parameter(component_id="order_required_param",
                                       location="query",
                                       component=self.search_params)

    def __order_by_required_params(self):
        self.spec.components.parameter(component_id="order_by_required_param",
                                       location="query",
                                       component=self.search_params)

    def active_params_default(self):
        self.__path_params_default()
        self.__page_params()
        self.__per_page_params()
        self.__search_params()