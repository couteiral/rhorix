# ParseTopology Python 3 Module
# Dr. Matthew J L Mills - Rhorix 1.0 - June 2017

def defineRadii():
    #Initial values taken from the old Java GUI - if not present, radius = 2.0
    elementRadii = \
    {
    "bcp"  : 0.75,
    "rcp"  : 0.75,
    "ccp"  : 0.75,
    "nacp" : 0.75,
    "ag"   : 1.72,
    "ar"   : 1.88,
    "as"   : 1.85,
    "au"   : 1.66,
    "b"    : 2.00,
    "br"   : 1.85,
    "c"    : 1.70,
    "cd"   : 1.58,
    "cl"   : 1.75,
    "cu"   : 1.40,
    "f"    : 1.47,
    "fe"   : 2.00,
    "ga"   : 1.87,
    "h"    : 1.20,
    "he"   : 1.40,
    "hg"   : 1.55,
    "i"    : 1.98,
    "in"   : 1.93,
    "k"    : 2.75,
    "kr"   : 2.02,
    "li"   : 1.82,
    "mg"   : 1.73,
    "n"    : 1.55,
    "na"   : 2.27,
    "ne"   : 1.54,
    "ni"   : 1.63,
    "o"    : 1.52,
    "p"    : 1.80,
    "pb"   : 2.02,
    "pd"   : 1.63,
    "pt"   : 1.72,
    "s"    : 1.80,
    "se"   : 1.90,
    "si"   : 2.10,
    "sn"   : 2.17,
    "te"   : 2.06,
    "tl"   : 1.96,
    "u"    : 1.86,
    "xe"   : 2.16,
    "zn"   : 1.39,
    }
    return elementRadii

def defineColors():
    #THESE ARE BORROWED FROM PYMOL - http://www.pymolwiki.org/index.php/Color_Values
    elementColors = \
    {
    "bcp"   :    ( 1.000000000,  0.000000000,  0.000000000),
    "ccp"   :    ( 0.000000000,  1.000000000,  0.000000000),
    "rcp"   :    ( 0.000000000,  0.000000000,  1.000000000),
    "nacp"  :    ( 1.000000000,  0.000000000,  0.000000000),
    "ac"    :    ( 0.439215686,  0.670588235,  0.980392157),
    "al"    :    ( 0.749019608,  0.650980392,  0.650980392),
    "am"    :    ( 0.329411765,  0.360784314,  0.949019608),
    "sb"    :    ( 0.619607843,  0.388235294,  0.709803922),
    "ar"    :    ( 0.501960784,  0.819607843,  0.890196078),
    "as"    :    ( 0.741176471,  0.501960784,  0.890196078),
    "at"    :    ( 0.458823529,  0.309803922,  0.270588235),
    "ba"    :    ( 0.000000000,  0.788235294,  0.000000000),
    "bk"    :    ( 0.541176471,  0.309803922,  0.890196078),
    "be"    :    ( 0.760784314,  1.000000000,  0.000000000),
    "bi"    :    ( 0.619607843,  0.309803922,  0.709803922),
    "bh"    :    ( 0.878431373,  0.000000000,  0.219607843),
    "b"     :    ( 1.000000000,  0.709803922,  0.709803922),
    "br"    :    ( 0.650980392,  0.160784314,  0.160784314),
    "cd"    :    ( 1.000000000,  0.850980392,  0.560784314),
    "ca"    :    ( 0.239215686,  1.000000000,  0.000000000),
    "cf"    :    ( 0.631372549,  0.211764706,  0.831372549),
    "c"     :    ( 0.269000000,  0.269000000,  0.269000000),
    "ce"    :    ( 1.000000000,  1.000000000,  0.780392157),
    "cs"    :    ( 0.341176471,  0.090196078,  0.560784314),
    "cl"    :    ( 0.121568627,  0.941176471,  0.121568627),
    "cr"    :    ( 0.541176471,  0.600000000,  0.780392157),
    "co"    :    ( 0.941176471,  0.564705882,  0.627450980),
    "cu"    :    ( 0.784313725,  0.501960784,  0.200000000),
    "cm"    :    ( 0.470588235,  0.360784314,  0.890196078),
    "db"    :    ( 0.819607843,  0.000000000,  0.309803922),
    "dy"    :    ( 0.121568627,  1.000000000,  0.780392157),
    "es"    :    ( 0.701960784,  0.121568627,  0.831372549),
    "er"    :    ( 0.000000000,  0.901960784,  0.458823529),
    "eu"    :    ( 0.380392157,  1.000000000,  0.780392157),
    "fm"    :    ( 0.701960784,  0.121568627,  0.729411765),
    "f"     :    ( 0.701960784,  1.000000000,  1.000000000),
    "fr"    :    ( 0.258823529,  0.000000000,  0.400000000),
    "gd"    :    ( 0.270588235,  1.000000000,  0.780392157),
    "ga"    :    ( 0.760784314,  0.560784314,  0.560784314),
    "ge"    :    ( 0.400000000,  0.560784314,  0.560784314),
    "au"    :    ( 1.000000000,  0.819607843,  0.137254902),
    "hf"    :    ( 0.301960784,  0.760784314,  1.000000000),
    "hs"    :    ( 0.901960784,  0.000000000,  0.180392157),
    "he"    :    ( 0.850980392,  1.000000000,  1.000000000),
    "ho"    :    ( 0.000000000,  1.000000000,  0.611764706),
    "h"     :    ( 0.900000000,  0.900000000,  0.900000000),
    "in"    :    ( 0.650980392,  0.458823529,  0.450980392),
    "i"     :    ( 0.580392157,  0.000000000,  0.580392157),
    "ir"    :    ( 0.090196078,  0.329411765,  0.529411765),
    "fe"    :    ( 0.878431373,  0.400000000,  0.200000000),
    "kr"    :    ( 0.360784314,  0.721568627,  0.819607843),
    "la"    :    ( 0.439215686,  0.831372549,  1.000000000),
    "lr"    :    ( 0.780392157,  0.000000000,  0.400000000),
    "pb"    :    ( 0.341176471,  0.349019608,  0.380392157),
    "li"    :    ( 0.800000000,  0.501960784,  1.000000000),
    "lu"    :    ( 0.000000000,  0.670588235,  0.141176471),
    "mg"    :    ( 0.541176471,  1.000000000,  0.000000000),
    "mn"    :    ( 0.611764706,  0.478431373,  0.780392157),
    "mt"    :    ( 0.921568627,  0.000000000,  0.149019608),
    "md"    :    ( 0.701960784,  0.050980392,  0.650980392),
    "hg"    :    ( 0.721568627,  0.721568627,  0.815686275),
    "mo"    :    ( 0.329411765,  0.709803922,  0.709803922),
    "nd"    :    ( 0.780392157,  1.000000000,  0.780392157),
    "ne"    :    ( 0.701960784,  0.890196078,  0.960784314),
    "np"    :    ( 0.000000000,  0.501960784,  1.000000000),
    "ni"    :    ( 0.313725490,  0.815686275,  0.313725490),
    "nb"    :    ( 0.450980392,  0.760784314,  0.788235294),
    "n"     :    ( 0.200000000,  0.200000000,  1.000000000),
    "no"    :    ( 0.741176471,  0.050980392,  0.529411765),
    "os"    :    ( 0.149019608,  0.400000000,  0.588235294),
    "o"     :    ( 1.000000000,  0.111000000,  0.075000000),
    "pd"    :    ( 0.000000000,  0.411764706,  0.521568627),
    "p"     :    ( 1.000000000,  0.501960784,  0.000000000),
    "pt"    :    ( 0.815686275,  0.815686275,  0.878431373),
    "pu"    :    ( 0.000000000,  0.419607843,  1.000000000),
    "po"    :    ( 0.670588235,  0.360784314,  0.000000000),
    "k"     :    ( 0.560784314,  0.250980392,  0.831372549),
    "pr"    :    ( 0.850980392,  1.000000000,  0.780392157),
    "pm"    :    ( 0.639215686,  1.000000000,  0.780392157),
    "pa"    :    ( 0.000000000,  0.631372549,  1.000000000),
    "ra"    :    ( 0.000000000,  0.490196078,  0.000000000),
    "rn"    :    ( 0.258823529,  0.509803922,  0.588235294),
    "re"    :    ( 0.149019608,  0.490196078,  0.670588235),
    "rh"    :    ( 0.039215686,  0.490196078,  0.549019608),
    "rb"    :    ( 0.439215686,  0.180392157,  0.690196078),
    "ru"    :    ( 0.141176471,  0.560784314,  0.560784314),
    "rf"    :    ( 0.800000000,  0.000000000,  0.349019608),
    "sm"    :    ( 0.560784314,  1.000000000,  0.780392157),
    "sc"    :    ( 0.901960784,  0.901960784,  0.901960784),
    "sg"    :    ( 0.850980392,  0.000000000,  0.270588235),
    "se"    :    ( 1.000000000,  0.631372549,  0.000000000),
    "si"    :    ( 0.941176471,  0.784313725,  0.627450980),
    "ag"    :    ( 0.752941176,  0.752941176,  0.752941176),
    "na"    :    ( 0.670588235,  0.360784314,  0.949019608),
    "sr"    :    ( 0.000000000,  1.000000000,  0.000000000),
    "s"     :    ( 0.900000000,  0.775000000,  0.250000000),
    "ta"    :    ( 0.301960784,  0.650980392,  1.000000000),
    "tc"    :    ( 0.231372549,  0.619607843,  0.619607843),
    "te"    :    ( 0.831372549,  0.478431373,  0.000000000),
    "tb"    :    ( 0.188235294,  1.000000000,  0.780392157),
    "tl"    :    ( 0.650980392,  0.329411765,  0.301960784),
    "th"    :    ( 0.000000000,  0.729411765,  1.000000000),
    "tm"    :    ( 0.000000000,  0.831372549,  0.321568627),
    "sn"    :    ( 0.400000000,  0.501960784,  0.501960784),
    "ti"    :    ( 0.749019608,  0.760784314,  0.780392157),
    "w"     :    ( 0.129411765,  0.580392157,  0.839215686),
    "u"     :    ( 0.000000000,  0.560784314,  1.000000000),
    "v"     :    ( 0.650980392,  0.650980392,  0.670588235),
    "xe"    :    ( 0.258823529,  0.619607843,  0.690196078),
    "yb"    :    ( 0.000000000,  0.749019608,  0.219607843),
    "y"     :    ( 0.580392157,  1.000000000,  1.000000000),
    "zn"    :    ( 0.490196078,  0.501960784,  0.690196078),
    "zr"    :    ( 0.580392157,  0.878431373,  0.878431373),
    }
    return elementColors
