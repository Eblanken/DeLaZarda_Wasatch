# This is the abstract base class for all Wasatch interface classes
class Wasatch_Serial_Interface_Abstract:
    #-------------------- Public Members ---------------

    # Initializes class and establishes serial with Wasatch
    def __init__(self):
        raise NotImplementedError("Subclass for Wasatch Interface must have its own initialization.")

    # Returns whether the microscope was able to establish a connection
    def connectedToMicroscope(self):
        raise NotImplementedError("Subclass for Wasatch Interface must have its own microscope state.")

    # Attempts to reestablish connection with the microscope
    def reconnectToMicroscope(self):
        raise NotImplementedError("Subclass for Wasatch Interface must have its own reconnection.")

    # Sends a serial command to the Wastach after 'time' milliseconds
    def sendCommand(self, command, time):
        raise NotImplementedError("Subclass for Wasatch Interface must have its own command method.")
