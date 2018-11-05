# -*- coding: utf-8 -*-

import os
import unittest
import vtk, qt, ctk, slicer
import logging
from I18nGuideletLoadable import I18nGuideletLoadable, I18nGuideletLogic, I18nGuideletTest, I18nGuideletWidget
from I18nGuideletLib import I18nGuidelet


class UsSimulatorTraining(I18nGuideletLoadable):
  """Uses GuideletLoadable class, available at:
  """

  def __init__(self, parent):
    I18nGuideletLoadable.__init__(self, parent)
    self.parent.title = "Us Simulation Navigation"
    self.parent.categories = ["USSimulator"]
    self.parent.dependencies = []
    self.parent.contributors = ["Carlos Luque (ULPGC)"]
    self.parent.helpText = """
    US simulations
    """
    self.parent.acknowledgementText = """
    NAMIC
    """ # replace with organization, grant and thanks.

class UsSimulatorTrainingWidget(I18nGuideletWidget):
  def __init__(self, parent = None):
    I18nGuideletWidget.__init__(self, parent) 
         # Creates the GuideletLogic 

  def setup(self):
    I18nGuideletWidget.setup(self)

  def addLauncherWidgets(self):
    I18nGuideletWidget.addLauncherWidgets(self)

  # this is invoked in onLaunchGuideletButtonClicked (SimulatorGuideletLoable.py)
  def createGuideletInstance(self):
    return UsSimulatorTrainingGuidelet(None, self.guideletLogic, self.selectedConfigurationName, self.selectedLanguage)

  def createGuideletLogic(self):
    return UsSimulatorTrainingLogic()

class UsSimulatorTrainingLogic(I18nGuideletLogic):
  """Uses GuideletLogic base class, available at:
  """ #TODO add path

  def __init__(self, parent = None):
    I18nGuideletLogic.__init__(self, parent)

class UsSimulatorTrainingTest(I18nGuideletTest):
  """This is the test case for your scripted module.
  """

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    I18nGuideletTest.runTest(self)
    
class UsSimulatorTrainingGuidelet(I18nGuidelet):

  def __init__(self, parent, logic, configurationName='Default', SelectedLanguage='English'):
    logging.debug('UsSimulatorTrainingGuidelet.__init__')
    I18nGuidelet.__init__(self, parent, logic, configurationName, SelectedLanguage)
    
    # Adds a default configurations to Slicer.ini
    self.logic.addValuesToDefaultConfiguration()

     # Set up main frame.
     # Dock Widget = tool palettes or utility windows
    self.sliceletDockWidget.setObjectName('UsSimulatorTrainingPanel')
    self.sliceletDockWidget.setWindowTitle('UsSimulatorTraining')
    self.mainWindow.setWindowTitle('UsSimulatorTraining')

 
  def __del__(self):#common
    self.cleanup()

  # Clean up when slicelet is closed
  def cleanup(self):#common
    I18nGuidelet.cleanup(self)
    logging.debug('cleanup')

  def createFeaturePanels(self):
    # Create GUI panels.
    logging.debug('UsSimulatorTraining.createFeaturePanels()')

    self.LoadSceneCollapsibleButton = ctk.ctkCollapsibleButton()
    self.SetupLoadSceneCollapsibleButton()

    featurePanelList = I18nGuidelet.createFeaturePanels(self)
    featurePanelList[len(featurePanelList):] = [self.LoadSceneCollapsibleButton]

    return featurePanelList

  def setupConnections(self):
    logging.debug('UsSimulatorTraining.setupConnections()')
    I18nGuidelet.setupConnections(self)

    self.LoadSceneButton.connect('clicked()', self.openLoadSceneDialog)

  def disconnect(self):#TODO see connect
    logging.debug('UsSimulatorTraining.disconnect()')
    I18nGuidelet.disconnect(self)
  
  def SetupLoadSceneCollapsibleButton(self):
    logging.debug('SetupLoadSceneCollapsibleButton')

    self.LoadSceneCollapsibleButton.setProperty('collapsedHeight', 20)
    self.LoadSceneCollapsibleButton.text = self.tr('Scene')
    self.sliceletPanelLayout.addWidget(self.LoadSceneCollapsibleButton)

    self.LoadSceneLayout = qt.QFormLayout(self.LoadSceneCollapsibleButton)
    self.LoadSceneLayout.setContentsMargins(12, 4, 4, 4)
    self.LoadSceneLayout.setSpacing(4)
  
    self.LoadSceneButton = qt.QPushButton(self.tr('Load Scene'))
    self.LoadSceneLayout.addRow(self.LoadSceneButton)


  def openLoadSceneDialog(self):
    slicer.app.ioManager().openLoadSceneDialog()
    self.layoutManager.setLayout(self.one2Ddual3dCustomLayoutId)
    self.setupConnectorNode()  # checking
    