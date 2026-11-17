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


def bt_dang14_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([25, 30, 35, 40])
        n = random.choice([144, 180, 216, 252, 288])
        r = (n * R) // 360
        kq_str = str(r)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một nghệ nhân làm nón lá cắt một tấm lá phẳng có dạng hình quạt tròn bán kính $%d\\text{ cm}$ với góc ở tâm là $%d^\\circ$, sau đó uốn cong và ghép hai bán kính lại với nhau (phần mép chồng lên nhau không đáng kể) để tạo thành phần thân nón có dạng hình nón. Tính bán kính đáy của chiếc nón lá tạo thành theo đơn vị $\\text{cm}$.
\\begin{center}
\\begin{tikzpicture}[scale=0.8]
\\fill[yellow!20] (0,0) -- (1.8,0) arc (0:216:1.8) -- cycle;
\\draw (0,0) -- (1.8,0) arc (0:216:1.8) -- cycle;
\\fill (0,0) circle (1.5pt);
\\node[below] at (0.9,0) {$R$};
\\node at (108:0.75) {$%d^\\circ$};
\\draw[->, thick] (2.2,0) -- (3.1,0);
\\begin{scope}[xshift=4.8cm, yshift=-0.6cm]
\\draw (-1.2,0) -- (0,1.7) -- (1.2,0);
\\draw (0,0) ellipse (1.2 and 0.35);
\\draw[dashed] (0,0) -- (1.2,0);
\\node[below] at (0.6,0) {$r$};
\\node[right] at (0.65,0.9) {$R$};
\\end{scope}
\\end{tikzpicture}
\\end{center}''' % (R, n, n))

        # Nội dung lời giải
        loigiai = ('''Độ dài cung tròn của tấm lá hình quạt tròn bán kính $R = %d\\text{ cm}$, góc ở tâm $%d^\\circ$ là:
$$l = \\dfrac{%d}{180}\\pi \\cdot %d = %d\\pi\\text{ (cm)}.$$
Khi uốn tấm lá thành hình nón, chu vi đường tròn đáy của chiếc nón bằng đúng độ dài cung tròn $l$. \\\\
Gọi $r$ ($\\text{cm}$) là bán kính đáy của chiếc nón, ta có:
$$2\\pi r = %d\\pi \\Leftrightarrow r = %d\\text{ (cm)}.$$''' % (
            R, n, n, R, 2 * r, 2 * r, r))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
