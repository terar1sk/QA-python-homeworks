import pytest


@pytest.mark.usefixtures("auth_session")
class TestCarsSearch:
    @pytest.mark.parametrize(
        "sort_by,limit",
        [
            ("price", 5),
            ("year", 10),
            ("engine_volume", 3),
            ("brand", 7),
            ("price", 1),
            (None, 5),
            ("year", None),
        ],
    )
    def test_cars_search_sort_and_limit(self, sort_by, limit):
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = str(limit)
        self.logger.info(f"GET /cars params={params}")
        r = self.session.get(f"{self.base_url}/cars", params=params, timeout=10)
        self.logger.info(f"GET /cars status={r.status_code} body_len={len(r.text)}")
        r.raise_for_status()
        data = r.json()
        assert isinstance(data, list), "Response should be a list"
        if limit is not None:
            assert len(data) <= limit
        if sort_by is not None:
            assert all(sort_by in car for car in data), f"Missing field {sort_by} in some items"
            values = [car[sort_by] for car in data]
            assert values == sorted(values), f"Cars are not sorted by {sort_by}"
        if data:
            self.logger.info(f"First item: {data[0]}")
            if len(data) > 1:
                self.logger.info(f"Second item: {data[1]}")