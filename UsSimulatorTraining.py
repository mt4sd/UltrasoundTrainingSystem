import os
import unittest
import vtk, qt, ctk, slicer
import logging
from Guidelet import GuideletLoadable, GuideletLogic, GuideletTest, GuideletWidget
from Guidelet import Guidelet
#
# UsSimulatorTraining
#
class UsSimulatorTraining(GuideletLoadable):
  """Uses GuideletLoadable class, available at:
  """

  def __init__(self, parent):
    GuideletLoadable.__init__(self, parent)
    self.parent.title = "US Simulation Navigation"
    self.parent.categories = ["IGT"]
    self.parent.dependencies = []
    self.parent.contributors = ["Carlos Luque (ULPGC), Csaba Pinter (Queen's)"]
    self.parent.helpText = """
    US simulations
    """
    self.parent.acknowledgementText = """
    NAMIC
    """ # replace with organization, grant and thanks.

#
# UsSimulatorTrainingWidget
#
class UsSimulatorTrainingWidget(GuideletWidget):
  def __init__(self, parent = None):
    GuideletWidget.__init__(self, parent)

  def setup(self):
    GuideletWidget.setup(self)

  def addLauncherWidgets(self):
    GuideletWidget.addLauncherWidgets(self)

  def createGuideletInstance(self):
    return UsSimulatorTrainingGuidelet(None, self.guideletLogic, self.selectedConfigurationName)

  def createGuideletLogic(self):
    return UsSimulatorTrainingLogic()

#
# UsSimulatorTrainingLogic
#
class UsSimulatorTrainingLogic(GuideletLogic):
  """Uses GuideletLogic base class, available at:
  """ #TODO add path

  def __init__(self, parent = None):
    GuideletLogic.__init__(self, parent)

#
# UsSimulatorTrainingTest
#
class UsSimulatorTrainingTest(GuideletTest):
  """This is the test case for your scripted module.
  """

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    GuideletTest.runTest(self)

#
# UsSimulatorTrainingGuidelet
#
class UsSimulatorTrainingGuidelet(Guidelet):

  VIEW_US_SIMULATOR_TRAINING = unicode("Ultrasound Simulator Training")

  def __init__(self, parent, logic, configurationName='Default'):
    Guidelet.__init__(self, parent, logic, configurationName)

    logging.debug('UsSimulatorTrainingGuidelet.__init__')
    self.logic.addValuesToDefaultConfiguration()

    # Set default layout name to the simulator training layout
    self.defaultLayoutName = self.VIEW_US_SIMULATOR_TRAINING

    # Set up main frame
    self.sliceletDockWidget.setObjectName('UsSimulatorTrainingPanel')
    self.sliceletDockWidget.setWindowTitle('UsSimulatorTraining')
    self.mainWindow.setWindowTitle('UsSimulatorTraining')

    self.selectView(self.VIEW_US_SIMULATOR_TRAINING)

  def __del__(self):
    self.cleanup()

  # Clean up when slicelet is closed
  def cleanup(self):
    Guidelet.cleanup(self)
    logging.debug('cleanup')

  def setupAdvancedPanel(self):
    Guidelet.setupAdvancedPanel(self)

    self.registerCustomLayouts()

  def registerCustomLayouts(self):
    customLayout = (
      "<layout type=\"horizontal\">"
        "<item>"
            "<view class=\"vtkMRMLSliceNode\" singletontag=\"Red\">"
            "  <property name=\"orientation\" action=\"default\">Axial</property>"
            "  <property name=\"viewlabel\" action=\"default\">R</property>"
            "  <property name=\"viewcolor\" action=\"default\">#F34A33</property>"
            "</view>"
        "</item>"
        "<item>"
            "<layout type=\"vertical\">"
              "<item>"
                "<view class=\"vtkMRMLViewNode\" singletontag=\"1\">"
                "<property name=\"viewlabel\" action=\"default\">1</property>"
                "</view>"
              "</item>"
              "<item>"
                "<view class=\"vtkMRMLViewNode\" singletontag=\"2\">"
                "<property name=\"viewlabel\" action=\"default\">2</property>"
                "</view>"
              "</item>"
            "</layout>"
        "</item>"
       "</layout>")

    self.registerLayout(self.VIEW_US_SIMULATOR_TRAINING, 525, customLayout, self.delayedFitAndHideUltrasoundSliceIn3dView)

  def createFeaturePanels(self):
    # Create GUI panels.
    logging.debug('UsSimulatorTraining.createFeaturePanels()')

    self.LoadSceneCollapsibleButton = ctk.ctkCollapsibleButton()
    self.SetupLoadSceneCollapsibleButton()

    featurePanelList = Guidelet.createFeaturePanels(self)

    featurePanelList[len(featurePanelList):] = [self.LoadSceneCollapsibleButton]

    return featurePanelList

  def setupConnections(self):
    logging.debug('UsSimulatorTraining.setupConnections()')
    Guidelet.setupConnections(self)

    self.LoadSceneButton.connect('clicked()', self.openLoadSceneDialog)

  def disconnect(self): #TODO: see connect
    logging.debug('UsSimulatorTraining.disconnect()')
    Guidelet.disconnect(self)

  def SetupLoadSceneCollapsibleButton(self):
    logging.debug('SetupLoadSceneCollapsibleButton')

    self.LoadSceneCollapsibleButton.setProperty('collapsedHeight', 20)
    self.LoadSceneCollapsibleButton.text = 'Scene'
    self.sliceletPanelLayout.addWidget(self.LoadSceneCollapsibleButton)

    self.LoadSceneLayout = qt.QFormLayout(self.LoadSceneCollapsibleButton)
    self.LoadSceneLayout.setContentsMargins(12, 4, 4, 4)
    self.LoadSceneLayout.setSpacing(4)

    self.LoadSceneButton = qt.QPushButton('Load Scene')
    self.LoadSceneLayout.addRow(self.LoadSceneButton)

  def openLoadSceneDialog(self):
    slicer.app.ioManager().openLoadSceneDialog()
    self.layoutManager.setLayout(self.one2Ddual3dCustomLayoutId)
    self.setupConnectorNode()  # checking
