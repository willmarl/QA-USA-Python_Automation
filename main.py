import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        #Check connection availability before running tests
        if not helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            raise Exception(f"URL {data.URBAN_ROUTES_URL} is not reachable. ")
        # Connection successful - tests will proceed
        print("Connected to the Urban Routes server")

    def test_set_route(self):
        # add in S8
        pass
    def test_select_plan(self):
        # add in S8
        pass
    def test_fill_phone_number(self):
        # add in S8
        pass
    def test_fill_card(self):
        # add in S8
        pass
    def test_comment_for_driver(self):
        # add in S8
        pass
    def test_order_blanket_and_handkerchiefs(self):
        # add in S8
        pass
    def test_order_2_ice_creams(self):
        for i in range(2):
            # Add in S8
            pass
    def test_car_search_model_appears(self):
        # add in S8
        pass