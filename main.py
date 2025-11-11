import data
import helpers

number_of_ice_creams = 2


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Check connection availability before running tests
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print(
                "Cannot connect to Urban Routes. Check the server is on and still running"
            )

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
        for i in range(number_of_ice_creams):
            # Add in S8
            pass

    def test_car_search_model_appears(self):
        # add in S8
        pass
