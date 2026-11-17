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



def bt_dang5_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R1 = randint(4, 7)
        R2 = randint(5, 8)
        R3 = randint(6, 9)
        a = R1 + R2
        b = R2 + R3
        c = R3 + R1
        chuvi = a + b + c
        nuachuvi = R1 + R2 + R3

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (0,0);
\\coordinate (O2) at (3.5,0);
\\coordinate (O3) at (1.5,3.1);
\\coordinate (M) at (1.5,0);
\\coordinate (N) at (2.64,1.33);
\\coordinate (P) at (0.65,1.35);
\\draw[line width=1pt] (O1) circle (1.5cm);
\\draw[line width=1pt] (O2) circle (2cm);
\\draw[line width=1pt] (O3) circle (1.94cm);
\\draw[line width=1pt] (O1)--(O2)--(O3)--cycle;
\\fill (O1) circle (1pt) node[below left] {$O_1$};
\\fill (O2) circle (1pt) node[below right] {$O_2$};
\\fill (O3) circle (1pt) node[above] {$O_3$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Cho ba đường tròn $(O_1; R_1)$, $(O_2; R_2)$ và $(O_3; R_3)$ đôi một tiếp xúc ngoài với nhau. Biết chu vi của tam giác $O_1O_2O_3$ bằng $%s\\text{ cm}$, đồng thời độ dài các cạnh của tam giác này lần lượt là $O_1O_2 = %s\\text{ cm}$, $O_2O_3 = %s\\text{ cm}$ và $O_3O_1 = %s\\text{ cm}$.\\\\
        a) Tính bán kính của mỗi đường tròn.\\\\
        b) Chứng minh rằng đường tròn nội tiếp tam giác $O_1O_2O_3$ đi qua ba tiếp điểm của ba đường tròn đã cho. %s'''
                         % (latex(chuvi), latex(a), latex(b), latex(c), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Vì ba đường tròn $(O_1; R_1)$, $(O_2; R_2)$ và $(O_3; R_3)$ đôi một tiếp xúc ngoài với nhau nên ta có hệ thức:\\\\
        $O_1O_2 = R_1 + R_2 = %s$; $O_2O_3 = R_2 + R_3 = %s$; $O_3O_1 = R_3 + R_1 = %s$.\\\\
        Cộng vế theo vế ba đẳng thức trên, ta được:\\\\
        $2(R_1 + R_2 + R_3) = %s + %s + %s = %s \\Rightarrow R_1 + R_2 + R_3 = %s$.\\\\
        Từ đó tính được:\\\\
        $R_1 = (R_1 + R_2 + R_3) - (R_2 + R_3) = %s - %s = %s\\text{ (cm)}$;\\\\
        $R_2 = (R_1 + R_2 + R_3) - (R_3 + R_1) = %s - %s = %s\\text{ (cm)}$;\\\\
        $R_3 = (R_1 + R_2 + R_3) - (R_1 + R_2) = %s - %s = %s\\text{ (cm)}$.
        \\item Gọi $M, N, P$ lần lượt là tiếp điểm của các cặp đường tròn $(O_1)$ và $(O_2)$, $(O_2)$ và $(O_3)$, $(O_3)$ và $(O_1)$.\\\\
        Do hai đường tròn tiếp xúc ngoài thì tiếp điểm nằm giữa hai tâm nên $M \\in O_1O_2$, $N \\in O_2O_3$, $P \\in O_3O_1$ và:\\\\
        $O_1M = O_1P = R_1$; $O_2M = O_2N = R_2$; $O_3N = O_3P = R_3$.\\\\
        Xét đường tròn nội tiếp tam giác $O_1O_2O_3$, giả sử đường tròn này tiếp xúc với các cạnh $O_1O_2, O_2O_3, O_3O_1$ tại $M', N', P'$. Theo tính chất hai tiếp tuyến cắt nhau, ta có $O_1M' = O_1P'$, $O_2M' = O_2N'$, $O_3N' = O_3P'$.\\\\
        Suy ra $O_1M' = \\frac{O_1O_2 + O_1O_3 - O_2O_3}{2} = \\frac{(R_1+R_2) + (R_1+R_3) - (R_2+R_3)}{2} = R_1 = O_1M$.\\\\
        Vì $M$ và $M'$ cùng thuộc đoạn $O_1O_2$ nên $M' \\equiv M$. Tương tự ta cũng có $N' \\equiv N$ và $P' \\equiv P$.\\\\
        Vậy đường tròn nội tiếp tam giác $O_1O_2O_3$ đi qua ba tiếp điểm $M, N, P$ của ba đường tròn đã cho.
        \\end{enumEX}'''
                   % (latex(a), latex(b), latex(c),
                      latex(a), latex(b), latex(c), latex(chuvi), latex(nuachuvi),
                      latex(nuachuvi), latex(b), latex(R1),
                      latex(nuachuvi), latex(c), latex(R2),
                      latex(nuachuvi), latex(a), latex(R3)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
