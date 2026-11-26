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


def bt_dang18_p3_b3_c7_ds8(self):
    # Dạng 18: Ứng dụng mặt phẳng tọa độ Oxy xác định khoảng cách đến vùng phủ sóng
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        bo_ba = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)])
        a, b, d_oh = bo_ba
        r_song = d_oh + random.randint(2, 8)
        kc_ranh_gioi = r_song - d_oh
        sx = random.choice([-1, 1])
        sy = random.choice([-1, 1])
        xh = sx * a
        yh = sy * b
        kq_str = str(kc_ranh_gioi)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.75, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (-2.8,0) -- (2.8,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-2.8) -- (0,2.8) node[left] {$y$};
\\draw[line width=1pt, dashed] (0,0) circle (2.2);
\\draw[line width=1pt] (0,0) -- (1.1,-1.1);
\\fill (0,0) circle (1pt) node[above left] {$O$};
\\fill (1.1,-1.1) circle (1pt) node[below right] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trên bản đồ quy hoạch đặt trên hệ trục tọa độ $Oxy$ (mỗi đơn vị trên trục ứng với $1\\text{ km}$ thực tế), một trạm phát sóng đặt tại gốc tọa độ $O(0;\\, 0)$ có bán kính phủ sóng tối đa là $%s\\text{ km}$. Một ngôi nhà đặt tại vị trí điểm $H(%s;\\, %s)$ (minh họa như hình vẽ). Khoảng cách từ ngôi nhà đó đến ranh giới vùng phủ sóng của trạm bằng bao nhiêu ki-lô-mét?
%s'''
                         % (r_song, xh, yh, tikz_code))

        loigiai = ('''Khoảng cách từ ngôi nhà tại $H(%s;\\, %s)$ đến trạm phát sóng tại $O(0;\\, 0)$ chính là độ dài đoạn thẳng $OH$. \\\\
Áp dụng định lí Pythagore trong hệ trục tọa độ vuông góc $Oxy$, ta có: \\\\
$OH = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s + %s} = \\sqrt{%s} = %s\\text{ (km)}$. \\\\
Vì $OH = %s\\text{ km} < %s\\text{ km}$ nên ngôi nhà nằm bên trong vùng phủ sóng của trạm. \\\\
Vậy khoảng cách từ ngôi nhà đó đến ranh giới vùng phủ sóng là: $%s - %s = %s\\text{ (km)}$.'''
                   % (xh, yh,
                      xh, yh, a**2, b**2, d_oh**2, d_oh,
                      d_oh, r_song,
                      r_song, d_oh, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
