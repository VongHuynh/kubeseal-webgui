from os import environ
from environmentvars import environmentVariables

class kubeseal:
  def __init__(self, controllername, controllernamespace):
    self.controllername = controllername
    self.controllernamespace = controllernamespace


  def getControllername(self):
    return self.controllername

  def getControllernamespace(self):
    return self.controllernamespace

  def getSealedSecretsControllerNamespace():
    return environmentVariables.getSealedSecretsControllerNamespace()

  def getSealedSecretsControllerName():
    return environmentVariables.getSealedSecretsControllerName()