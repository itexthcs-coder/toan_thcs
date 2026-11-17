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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D



def bt_dang1_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = randint(3, 6)
        R = r + randint(3, 6)

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (O') at (1.5,0);
\\coordinate (O) at (3,0);
\\coordinate (E) at (3,0);
\\coordinate (D) at (6,0);
\\coordinate (B) at (2.1,1.374);
\\coordinate (C) at (4.2,2.749);
\\draw[line width=1pt] (O) circle (3cm);
\\draw[line width=1pt] (O') circle (1.5cm);
\\draw[line width=1pt] (A)--(D) (A)--(C) (O')--(B) (O)--(C) (E)--(B) (D)--(C);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (O') circle (1pt) node[below] {$O'$};
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc trong tại điểm $A$. Một đường thẳng đi qua $A$ (không đi qua tâm) cắt $(O')$ tại $B$ và cắt $(O)$ tại $C$.\\\\
        a) Chứng minh rằng $O'B // OC$.\\\\
        b) Vẽ đường kính $AD$ của $(O)$ và đường kính $AE$ của $(O')$. Chứng minh tứ giác $EBCD$ có $EB // DC$. %s'''
                         % (latex(R), latex(r), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc trong tại $A$ nên ba điểm $O, O', A$ thẳng hàng và $O'$ nằm giữa $O$ và $A$.\\\\
        Xét tam giác $O'AB$ có $O'A = O'B = %s\\text{ cm}$ nên tam giác $O'AB$ cân tại $O'$, suy ra $\\widehat{O'AB} = \\widehat{O'BA}$.\\\\
        Xét tam giác $OAC$ có $OA = OC = %s\\text{ cm}$ nên tam giác $OAC$ cân tại $O$, suy ra $\\widehat{OAC} = \\widehat{OCA}$.\\\\
        Vì $O'$ nằm giữa $O$ và $A$, $B$ nằm giữa $A$ và $C$ nên $\\widehat{O'AB}$ và $\\widehat{OAC}$ là cùng một góc. Do đó $\\widehat{O'BA} = \\widehat{OCA}$.\\\\
        Hai góc này ở vị trí đồng vị nên suy ra $O'B // OC$.
        \\item Xét tam giác $ABE$ có $O'$ là trung điểm của đường kính $AE$ và $B \\in (O')$ nên đường trung tuyến $BO' = \\frac{1}{2}AE$. Do đó tam giác $ABE$ vuông tại $B$, suy ra $EB \\perp AC$.\\\\
        Tương tự, xét tam giác $ACD$ có $O$ là trung điểm của đường kính $AD$ và $C \\in (O)$ nên đường trung tuyến $CO = \\frac{1}{2}AD$. Do đó tam giác $ACD$ vuông tại $C$, suy ra $DC \\perp AC$.\\\\
        Vì $EB$ và $DC$ cùng vuông góc với đường thẳng $AC$ nên $EB // DC$.
        \\end{enumEX}'''
                   % (latex(R), latex(r), latex(r), latex(R)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
