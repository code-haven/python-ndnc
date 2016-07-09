from ndnc.main import httpCall


def test_httpCall():
    assert(httpCall() == 200)