class Bomb:
    serial = ""
    batteries = ""
    ports = []

    # Modules will hold name and location on bomb
    modules = []

    # Physical state will keep track of what is
    # being looked at on the bomb. That way, you
    # can go from any module to any other.
    # This should only be manipulated by
    # modules/controller/macro.py
    physical_state = None
