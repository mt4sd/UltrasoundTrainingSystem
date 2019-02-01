cmake_minimum_required(VERSION 3.5)

project(UltrasoundTrainingSystem)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/mt4sd/UltrasoundTrainingSystem")
set(EXTENSION_CATEGORY "IGT")
set(EXTENSION_CONTRIBUTORS "Carlos Luque (ULPGC), Csaba Pinter (Queen's University)")
set(EXTENSION_DESCRIPTION "")
set(EXTENSION_ICONURL "https://github.com/mt4sd/UltrasoundTrainingSystem/raw/master/Resources/Icons/UltrasoundTrainingSystem.png")
set(EXTENSION_SCREENSHOTURLS "")
set(EXTENSION_DEPENDS SlicerIGT SlicerOpenIGTLink) # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
set(MODULE_NAME UltrasoundTrainingSystem)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
  )

set(MODULE_PYTHON_RESOURCES
  Resources/Icons/${MODULE_NAME}.png
  )

#-----------------------------------------------------------------------------
slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_PYTHON_SCRIPTS}
  RESOURCES ${MODULE_PYTHON_RESOURCES}
  #WITH_GENERIC_TESTS
  )

#-----------------------------------------------------------------------------
if(BUILD_TESTING)

  # Register the unittest subclass in the main script as a ctest.
  # Note that the test will also be available at runtime.
  slicer_add_python_unittest(SCRIPT ${MODULE_NAME}.py)

  # Additional build-time testing
  #add_subdirectory(Testing)
endif()

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
