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


def bt_dang17_p3_b1_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Phép lai sinh học 3 cặp gene: bố (Aa, Bb, Dd) x mẹ (AA, Bb, dd) -> số kiểu gene trong không gian mẫu
        truong_hop = [
            ('(Aa, Bb, Dd)', '(AA, Bb, dd)', 2, 4, 2, 16,
             'Cặp $Aa \\times AA$ cho $2$ tổ hợp ($AA; Aa$). Cặp $Bb \\times Bb$ cho $4$ tổ hợp ($BB; Bb; bB; bb$). Cặp $Dd \\times dd$ cho $2$ tổ hợp ($Dd; dd$).'),
            ('(Aa, Bb, Dd)', '(Aa, Bb, Dd)', 4, 4, 4, 64,
             'Mỗi cặp $Aa \\times Aa$, $Bb \\times Bb$, $Dd \\times Dd$ đều cho $4$ tổ hợp giao tử phân biệt nguồn gốc bố mẹ.'),
            ('(AA, Bb, Dd)', '(Aa, BB, Dd)', 2, 2, 4, 16,
             'Cặp $AA \\times Aa$ cho $2$ tổ hợp. Cặp $Bb \\times BB$ cho $2$ tổ hợp. Cặp $Dd \\times Dd$ cho $4$ tổ hợp.'),
            ('(Aa, bb, Dd)', '(aa, Bb, Dd)', 2, 2, 4, 16,
             'Cặp $Aa \\times aa$ cho $2$ tổ hợp. Cặp $bb \\times Bb$ cho $2$ tổ hợp. Cặp $Dd \\times Dd$ cho $4$ tổ hợp.')
        ]
        bo, me, c1, c2, c3, ans, gt = random.choice(truong_hop)
        kq_str = str(ans)
        noidungcauhoi = ('''Ở một loài thực vật, xét ba cặp gene phân li độc lập quy định ba tính trạng khác nhau. Khi lai hai cây bố mẹ, cây con nhận ngẫu nhiên $1$ gene từ cây bố và $1$ gene từ cây mẹ ở mỗi cặp tính trạng. Thực hiện phép thử cho lai cây bố có kiểu gene $%s$ với cây mẹ có kiểu gene $%s$. Không gian mẫu về tổ hợp kiểu gene ở đời con có bao nhiêu phần tử?'''
                         % (bo, me))
        loigiai = ('''Xét riêng từng cặp gene theo thứ tự (gene từ bố, gene từ mẹ):\\\\
%s\\\\
Theo quy tắc nhân, số phần tử của không gian mẫu là $%s \\cdot %s \\cdot %s = %s$.'''
                   % (gt, c1, c2, c3, ans))
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
