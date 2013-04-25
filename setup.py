import sys

if sys.platform == 'win32':
    # ======================================================== #
    # File automagically generated by GUI2Exe version 0.5.3
    # Copyright: (c) 2007-2012 Andrea Gavana
    # ======================================================== #
    
    # Let's start with some default (for me) imports...
    
    from distutils.core import setup
    from py2exe.build_exe import py2exe
    
    import glob
    import os
    import zlib
    import shutil
    
    # Remove the build folder
    shutil.rmtree("build", ignore_errors=True)
    
    
    class Target(object):
        """ A simple class that holds information on our executable file. """
        def __init__(self, **kw):
            """ Default class constructor. Update as you need. """
            self.__dict__.update(kw)
            
    
    # Ok, let's explain why I am doing that.
    # Often, data_files, excludes and dll_excludes (but also resources)
    # can be very long list of things, and this will clutter too much
    # the setup call at the end of this file. So, I put all the big lists
    # here and I wrap them using the textwrap module.
    
    data_files = [('', ['expressionTopology.ui'])]
    
    includes = ['PySide.QtCore', 'PySide.QtGui', 'PySide.QtXml', 'PySide.QtUiTools']
    excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
                'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                'Tkconstants', 'Tkinter']
    packages = []
    dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'MSVCP90.dll',
                    'tcl84.dll', 'tk84.dll']
    icon_resources = [(1, 'icon.ico')]
    bitmap_resources = []
    other_resources = []
    
    
    # This is a place where the user custom code may go. You can do almost
    # whatever you want, even modify the data_files, includes and friends
    # here as long as they have the same variable name that the setup call
    # below is expecting.
    
    # No custom code added
    
    
    # Ok, now we are going to build our target class.
    # I chose this building strategy as it works perfectly for me :-D
    
    GUI2Exe_Target_1 = Target(
        # what to build
        script = "expressionTopology.py",
        icon_resources = icon_resources,
        bitmap_resources = bitmap_resources,
        other_resources = other_resources,
        dest_base = "expressionTopology",    
        version = "1.0",
        company_name = "University of Utah",
        copyright = "2013",
        name = "expressionTopology",
        
        )
    
    # No custom class for UPX compression or Inno Setup script
    
    # That's serious now: we have all (or almost all) the options py2exe
    # supports. I put them all even if some of them are usually defaulted
    # and not used. Some of them I didn't even know about.
                        
    setup(
    
        # No UPX or Inno Setup
    
        data_files = data_files,
    
        options = {"py2exe": {"compressed": 0, 
                              "optimize": 0,
                              "includes": includes,
                              "excludes": excludes,
                              "packages": packages,
                              "dll_excludes": dll_excludes,
                              "bundle_files": 3,
                              "dist_dir": "dist",
                              "xref": False,
                              "skip_archive": False,
                              "ascii": False,
                              "custom_boot_script": '',
                             }
                  },
    
        zipfile = None,
        console = [],
        windows = [GUI2Exe_Target_1],
        service = [],
        com_server = [],
        ctypes_com_server = []
        )
    
    # This is a place where any post-compile code may go.
    # You can add as much code as you want, which can be used, for example,
    # to clean up your folders or to do some particular post-compilation
    # actions.
    
    # No post-compilation code added
    
    
    # And we are done. That's a setup script :-D
elif sys.platform == 'darwin':
    # ======================================================== #
    # File automagically generated by GUI2Exe version 0.5.3
    # Copyright: (c) 2007-2012 Andrea Gavana
    # ======================================================== #
    
    # Let's start with some default (for me) imports...
    
    from setuptools import setup
    
    
    # Ok, let's explain why I am doing that.
    # Often, data_files, excludes and friends (but also resources)
    # can be very long list of things, and this will clutter too much
    # the setup call at the end of this file. So, I put all the big lists
    # here and I wrap them using the textwrap module.
    
    resources = ['expressionTopology.ui']
    
    includes = ['PySide.QtCore', 'PySide.QtGui', 'PySide.QtXml', 'PySide.QtUiTools']
    excludes = ['Tkconstants', 'Tkinter', '_gtkagg', '_tkagg', 'bsddb',
                'curses', 'email', 'pywin.debugger', 'pywin.debugger.dbgcon',
                'pywin.dialogs', 'tcl']
    packages = []
    frameworks = []
    dylib_excludes = []
    datamodels = []
    
    # PList custom code (if any) goes here
    # No code for PList
    
    # This is a place where the user custom code may go. You can do almost
    # whatever you want, even modify the data_files, includes and friends
    # here as long as they have the same variable name that the setup call
    # below is expecting.
    
    # No custom code added
    
    
    # That's serious now: we have all (or almost all) the options py2app
    # supports. I put them all even if some of them are usually defaulted
    # and not used. Some of them I didn't even know about.
    
    setup(
    
        app = [r'expressionTopology.py'],
        setup_requires=['py2app'],
        
        options = {"py2app": {"optimize": 0,
                              "includes": includes,
                              "excludes": excludes,
                              "packages": packages,
                              "dylib_excludes": dylib_excludes,
                              "frameworks": frameworks,
                              "datamodels": datamodels,
                              "resources": resources,
                              "iconfile": r'icon.icns',
                              "plist": None,
                              "extension": ".app",
                              "graph": False,
                              "dist_dir": r"dist",
                              "xref": False,
                              "no_strip": False,
                              "no_chdir": False,
                              "semi_standalone": False,
                              "argv_emulation": True,
                              "use_pythonpath": False,
                              "site_packages": False,
                              "prefer_ppc": False,
                              "debug_modulegraph": False,
                              "debug_skip_macholib": False
                             }
                  },
        )
    
    # This is a place where any post-compile code may go.
    # You can add as much code as you want, which can be used, for example,
    # to clean up your folders or to do some particular post-compilation
    # actions.
    
    # No post-compilation code added
    
    
    # And we are done. That's a setup script :-D
elif sys.platform == 'linux2':
    # ======================================================== #
    # File automagically generated by GUI2Exe version 0.5.3
    # Copyright: (c) 2007-2012 Andrea Gavana
    # ======================================================== #
    
    # Let's start with some default (for me) imports...
    
    from cx_Freeze import setup, Executable
    import PySide.QtCore
    
    
    # Process the includes, excludes and packages first
    
    includes = ['PySide.QtCore', 'PySide.QtGui', 'PySide.QtXml', 'PySide.QtUiTools']
    excludes = ['bsddb', 'curses', 'email', '_gtkagg', 'pywin.debugger',
                'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                '_tkagg', 'Tkconstants', 'Tkinter']
    packages = []
    path = []
    
    # This is a place where the user custom code may go. You can do almost
    # whatever you want, even modify the data_files, includes and friends
    # here as long as they have the same variable name that the setup call
    # below is expecting.
    
    # No custom code added
    
    # The setup for cx_Freeze is different from py2exe. Here I am going to
    # use the Python class Executable from cx_Freeze
    
    
    GUI2Exe_Target_1 = Executable(
        # what to build
        script = "expressionTopology.py",
        initScript = None,
        base = None,
        targetDir = r"dist",
        targetName = "expressionTopology",
        compress = True,
        copyDependentFiles = False,
        appendScriptToExe = False,
        appendScriptToLibrary = False,
        icon = r"icon.png"
        )
    
    
    # That's serious now: we have all (or almost all) the options cx_Freeze
    # supports. I put them all even if some of them are usually defaulted
    # and not used. Some of them I didn't even know about.
    print includes
    setup(
        
        version = "1.0",
        description = "No Description",
        author = "Alex Bigelow",
        name = "expressionTopology",
        options = {"build_exe": {"includes": includes,
                                 "excludes": excludes,
                                 "packages": packages,
                                 "path": path
                                 }
                   },
                               
        executables = [GUI2Exe_Target_1]
        )
    
    # This is a place where any post-compile code may go.
    # You can add as much code as you want, which can be used, for example,
    # to clean up your folders or to do some particular post-compilation
    # actions.
    
    # No post-compilation code added
    
    
    # And we are done. That's a setup script :-D
    print 'd'
    
else:
    print "Building an executable for platform %s is not supported yet!" % sys.platform
    print "You should be able to run the app by typing:"
    print ""
    print "python compreheNGSive.py"
    print ""
    print "at the command line. If you want to help out, feel free to"
    print "add to setup.py and/or see http://sci.utah.edu/~abigelow/compreheNGSive.php"
    sys.exit(1)


