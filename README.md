# RhoRix (QCT For Blender)

RhoRix is a [Blender](http://www.blender.org) *Add-On* (i.e. a script that extends Blender with extra functionality) that allows the user to import files containing topological objects defined by the theory of [Quantum Chemical Topology](http://www.chemistry.mcmaster.ca/bader/) (QCT). The program converts topological data to 3D objects, and subsequently the full functionality of Blender can be used to render images of the topology. Note that the purpose of this program is to enable import of (and provide a standard appearance for) a topology, and the user is encouraged to consult the full Blender documentation and tutorials in order to obtain creative renders.

The Add-On's Python code is written to adhere to the [Pep-8 Guidelines](http://www.python.org/dev/peps/pep-0008/#introduction).
The initial code was written with reference to Chapter 4 of the WikiBook '[Blender 3D: Noob to Pro](http://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro#Table_of_Contents/)' and the appropriate section of the [Blender documentation](https://docs.blender.org/api/blender_python_api_2_78c_release/).
Significant Perl code is provided for conversion of the output of standard QCT programs to the included XML-based filetype. These scripts are provided as a set of traditional modules (sets of subroutines for import).

Full documentation is provided in 'Manual.pdf', 'QuickStart.pdf' and a peer-reviewed paper.


#### Using the Program

The entire package should be installed by placing the files into your Blender user preferences directory, which will cause Rhorix to appear in the Add-Ons list in the User Preferences window. Doing this directly is OS-dependent and users are advised to consult the Blender documentation. The script will add an operator named 'Import Topology' to the built-in list that can be accessed by pressing the spacebar with the 3D view active. Additionally, the operator is added as a menu item under File -> Import -> Quantum Chemical Topology (.top). Finally, a panel will appear in the left-hand side of the 3D view with an 'Import Topology' button. No keyboard shortcuts are defined.

#### Copyright Message

Rhorix Copyright (c) 2017, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy).  All rights reserved.
 
If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Innovation and Partnerships department at IPO@lbl.gov referring to " Rhorix (2017-158)."
 
NOTICE.  This software was developed under funding from the U.S. Department of Energy.  As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, prepare derivative works, and perform publicly and display publicly. The U.S. Government is granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, prepare derivative works, distribute copies to the public, perform publicly and display publicly, and to permit others to do so.
