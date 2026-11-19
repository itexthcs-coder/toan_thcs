# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang13_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.3,2.5);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.2,0);
\\coordinate (D) at (1.3,0);
\\coordinate (E) at (2.11,1.43);
\\coordinate (F) at (0.64,1.23);
\\coordinate (H) at (intersection of B--E and C--F);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(D) (B)--(E) (C)--(F);
\\draw[line width=1pt, dashed] (E)--(F);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\fill (F) circle (1pt) node[above left] {$F$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho tam giác nhọn $ABC$ ($AB < AC$) có ba đường cao $AD, BE, CF$ cắt nhau tại trực tâm $H$ (như hình vẽ). \\
a) Chứng minh rằng các tứ giác $BFEC$ và $AEHF$ là các tứ giác nội tiếp. \\
b) Giả sử $\\widehat{BAC} = 60^\\circ$, hãy tính số đo góc $\\widehat{EHF}$ và chứng minh $EF = \\frac{1}{2}BC$. %s'''
                         % (hinh_tikz))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\item Vì $BE, CF$ là các đường cao của $\\triangle ABC$ nên $\\widehat{BFC} = \\widehat{BEC} = 90^\\circ$. \\
Hai đỉnh $E, F$ cùng nhìn cạnh $BC$ dưới một góc vuông nên $E, F$ cùng nằm trên đường tròn đường kính $BC$. Vậy tứ giác $BFEC$ nội tiếp đường tròn đường kính $BC$. \\
Xét tứ giác $AEHF$ có $\\widehat{AFH} + \\widehat{AEH} = 90^\\circ + 90^\\circ = 180^\\circ$. Vì tổng hai góc đối nhau bằng $180^\\circ$ nên tứ giác $AEHF$ nội tiếp đường tròn đường kính $AH$.
\item Khi $\\widehat{BAC} = 60^\\circ$, vì tứ giác $AEHF$ nội tiếp nên $\\widehat{EHF} = 180^\\circ - \\widehat{EAF} = 180^\\circ - 60^\\circ = 120^\\circ$. \\
Xét tam giác vuông $ABE$ vuông tại $E$ có $\\widehat{BAE} = 60^\\circ$ nên $AE = AB \\cdot \\cos 60^\\circ = \\frac{1}{2}AB$. \\
Xét $\\triangle AEF$ và $\\triangle ABC$ có $\\widehat{EAF} = \\widehat{BAC} = 60^\\circ$ và $\\frac{AE}{AB} = \\frac{AF}{AC} = \\cos 60^\\circ = \\frac{1}{2}$, nên $\\triangle AEF \\backsim \\triangle ABC$ (c.g.c) theo tỉ số đồng dạng $\\frac{1}{2}$. \\
Vậy $EF = \\frac{1}{2}BC$.
\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
