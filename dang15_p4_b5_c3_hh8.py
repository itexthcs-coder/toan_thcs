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


def bt_dang15_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([(6, 8), (8, 12), (10, 14), (4, 10), (12, 16)])
        ab, ac = bo_so
        canh_hv = (ab + ac) // 2
        dien_tich = canh_hv ** 2

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,2.0);
\\coordinate (C) at (2.8,0);
\\coordinate (D) at (4.8,2.8);
\\coordinate (E) at (2.0,4.8);
\\coordinate (O) at (2.4,2.4);
\\coordinate (M) at (0,2.4);
\\coordinate (N) at (2.4,0);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(C)--(D)--(E)--cycle (B)--(D) (C)--(E) (A)--(O) (O)--(M) (O)--(N);
\\draw[line width=1pt, dashed] (B)--(M);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (E) circle (1pt) node[above] {$E$};
\\fill (O) circle (1pt) node[above right] {$O$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $\\Delta ABC$ vuông tại $A$ ($AB < AC$). Vẽ ra phía ngoài tam giác đó hình vuông $BCDE$. Gọi $O$ là giao điểm hai đường chéo của hình vuông $BCDE$. \\\\
a) Hạ $OM \\perp AB$ ($M \\in AB$) và $ON \\perp AC$ ($N \\in AC$). Chứng minh tứ giác $AMON$ là hình vuông. \\\\
b) Chứng minh tia $AO$ là tia phân giác của góc vuông $\\widehat{BAC}$ và $AO \\perp BC$. \\\\
c) Biết $AB = %s\\text{ cm}, AC = %s\\text{ cm}$, tính diện tích của hình vuông $AMON$.%s'''
                         % (ab, ac, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Tứ giác $AMON$ có $\\widehat{A} = \\widehat{AMO} = \\widehat{ANO} = 90^\\circ$ nên là hình chữ nhật.\\\\
Vì $O$ là giao điểm hai đường chéo của hình vuông $BCDE$ nên $OB = OC$ và $\\widehat{BOC} = 90^\\circ$.\\\\
Ta có $\\widehat{MOB} + \\widehat{BON} = 90^\\circ$ (do $MONB$ có $\\widehat{MON} = 90^\\circ$) và $\\widehat{NOC} + \\widehat{BON} = \\widehat{BOC} = 90^\\circ$, suy ra $\\widehat{MOB} = \\widehat{NOC}$.\\\\
Xét hai tam giác vuông $\\Delta OBM$ và $\\Delta OCN$ có: $\\widehat{OMB} = \\widehat{ONC} = 90^\\circ$, $OB = OC$, $\\widehat{MOB} = \\widehat{NOC}$.\\\\
Suy ra $\\Delta OBM = \\Delta OCN$ (c.h - g.n), do đó $OM = ON$.\\\\
Hình chữ nhật $AMON$ có hai cạnh kề bằng nhau nên là hình vuông.
\\item Vì $AMON$ là hình vuông nên đường chéo $AO$ là tia phân giác của góc vuông $\\widehat{BAC}$, suy ra $\\widehat{BAO} = 45^\\circ$.\\\\
Gọi $H$ là giao điểm của $AO$ và $BC$. Vì $\\Delta OBC$ vuông cân tại $O$ nên $\\widehat{OBC} = 45^\\circ$.\\\\
Trong $\\Delta ABH$, ta có $\\widehat{AHB} = 180^\\circ - (\widehat{BAH} + \\widehat{ABH}) = 180^\\circ - (45^\\circ + \\widehat{ABC} + 45^\\circ) = 90^\\circ - \\widehat{ABC}$... Xét trực tiếp $\\Delta OBH$ và $\\Delta AHC$: $\\widehat{OBH} = 45^\\circ = \\widehat{HAC}$ và $\\widehat{BHO} = \\widehat{AHC}$ (đối đỉnh), suy ra $\\widehat{BHO} = 90^\\circ$, hay $AO \\perp BC$.
\\item Từ $\\Delta OBM = \\Delta OCN$ suy ra $BM = CN$.\\\\
Vì $AMON$ là hình vuông nên $AM = AN$.\\\\
Ta có $AB + AC = (AM - BM) + (AN + CN) = AM + AN = 2AM$ (do $BM = CN$).\\\\
Suy ra $AM = \\dfrac{AB + AC}{2} = \\dfrac{%s + %s}{2} = %s\\text{ (cm)}$.\\\\
Vậy diện tích hình vuông $AMON$ là $S_{AMON} = AM^2 = %s^2 = %s\\text{ (cm}^2)$.
\\end{enumEX} \n'''
                   % (ab, ac, canh_hv, canh_hv, dien_tich))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
