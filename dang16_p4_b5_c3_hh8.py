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


def bt_dang16_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (2.6,2.6);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at (1.3,2.6);
\\coordinate (N) at (2.6,1.3);
\\coordinate (I) at (2.08,2.08);
\\coordinate (K) at (-1.3,0);
\\coordinate (P) at (1.3,0);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (C)--(M) (D)--(N);
\\draw[line width=1pt, dashed] (A)--(I) (D)--(K) (A)--(K) (M)--(P);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (I) circle (1pt) node[above left] {$I$};
\\fill (K) circle (1pt) node[left] {$K$};
\\fill (P) circle (1pt) node[below] {$P$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình vuông $ABCD$. Gọi $M$ là trung điểm của $AB$, $N$ là trung điểm của $BC$. Giao điểm của $CM$ và $DN$ là $I$. \\\\
a) Chứng minh $CM \\perp DN$ tại $I$. \\\\
b) Chứng minh $AI = AD$. \\\\
c) Trên tia đối của tia $DC$ lấy điểm $K$ sao cho $DK = BM$. Chứng minh $AK \\perp CM$.%s'''
                         % (hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Xét hai tam giác vuông $\\Delta MBC$ và $\\Delta NCD$ có: $MB = NC$ (cùng bằng nửa cạnh hình vuông), $\\widehat{B} = \\widehat{C} = 90^\\circ$, $BC = CD$.\\\\
Suy ra $\\Delta MBC = \\Delta NCD$ (c.g.c), do đó $\\widehat{MCB} = \\widehat{NDC}$.\\\\
Mà $\\widehat{NDC} + \\widehat{DNC} = 90^\\circ$ nên $\\widehat{MCB} + \\widehat{DNC} = 90^\\circ$, suy ra $\\widehat{NIC} = 90^\\circ$, hay $CM \\perp DN$ tại $I$.
\\item Gọi $P$ là trung điểm của $CD$. Tứ giác $AMCP$ có $AM // CP$ và $AM = CP$ nên là hình bình hành, suy ra $AP // CM$.\\\\
Vì $CM \\perp DN$ nên $AP \\perp DN$.\\\\
Xét $\\Delta DCI$ vuông tại $I$ có $P$ là trung điểm của $CD$, đường thẳng qua $P$ song song với $CI$ cắt $DI$ tại trung điểm của $DI$.\\\\
Do đó $AP$ vừa là đường cao vừa là đường trung tuyến của $\\Delta ADI$, suy ra $\\Delta ADI$ cân tại $A$, vậy $AI = AD$.
\\item Xét hai tam giác vuông $\\Delta ADK$ và $\\Delta CBM$ có: $AD = CB$, $\\widehat{ADK} = \\widehat{CBM} = 90^\\circ$, $DK = BM$ (giả thiết).\\\\
Suy ra $\\Delta ADK = \\Delta CBM$ (c.g.c), do đó $\\widehat{DAK} = \\widehat{BCM}$.\\\\
Mặt khác $\\widehat{BCM} + \\widehat{BMC} = 90^\\circ$ và $\\widehat{BMC} = \\widehat{MCD}$ (so le trong) nên $\\widehat{DAK} + \\widehat{MCD} = 90^\\circ$.\\\\
Trong tam giác tạo bởi $AK, CM$ và $CD$, tổng hai góc nhọn bằng $90^\\circ$ nên góc còn lại bằng $90^\\circ$, vậy $AK \\perp CM$.
\\end{enumEX} \n''')

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
