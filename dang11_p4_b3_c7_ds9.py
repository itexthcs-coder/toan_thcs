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


def bt_dang11_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        noidungcauhoi = ('''Một nông trường trồng thử nghiệm hai giống lúa mới OM18 và ST25 trên các thửa ruộng có cùng diện tích và thu được kết quả về năng suất (đơn vị: tạ/ha) như sau:
\\begin{itemize}
\\item Giống OM18 ($50$ thửa): $[55; 60)$ có $8$ thửa; $[60; 65)$ có $22$ thửa; $[65; 70)$ có $15$ thửa; $[70; 75)$ có $5$ thửa.
\\item Giống ST25 ($40$ thửa): $[55; 60)$ có $4$ thửa; $[60; 65)$ có $12$ thửa; $[65; 70)$ có $16$ thửa; $[70; 75)$ có $8$ thửa.
\\end{itemize}
a) Lập bảng tần số tương đối ghép nhóm cho từng giống lúa.\\
b) Dựa vào bảng tần số tương đối ghép nhóm, hãy so sánh năng suất của hai giống lúa OM18 và ST25.''')

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tính tần số tương đối cho từng giống lúa (OM18 chia cho $50$, ST25 chia cho $40$), ta có bảng tần số tương đối ghép nhóm tổng hợp:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Năng suất (tạ/ha) & $[55; 60)$ & $[60; 65)$ & $[65; 70)$ & $[70; 75)$ \\\\
\\hline
Giống OM18 & $16\\%%$ & $44\\%%$ & $30\\%%$ & $10\\%%$ \\\\
\\hline
Giống ST25 & $10\\%%$ & $30\\%%$ & $40\\%%$ & $20\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item So sánh năng suất:
\\begin{itemize}
\\item Tỉ lệ thửa ruộng đạt năng suất cao từ $65$ tạ/ha trở lên ở giống ST25 là $40\\%% + 20\\%% = 60\\%%$, cao hơn hẳn so với giống OM18 ($30\\%% + 10\\%% = 40\\%%$).
\\item Tỉ lệ thửa ruộng năng suất thấp dưới $60$ tạ/ha của giống ST25 ($10\\%%$) cũng thấp hơn giống OM18 ($16\\%%$).
\\item Kết luận: Giống lúa ST25 cho năng suất vượt trội hơn giống OM18 trong đợt trồng thử nghiệm này.
\\end{itemize}
\\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
