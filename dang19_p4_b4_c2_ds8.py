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


def bt_dang19_p4_b4_c2_ds8(self):
    P = symbols('P')
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p_val = random.choice([100, 200, 500])
        lai_phan_tram = random.choice([5, 6, 8])
        x_dec = Decimal(str(lai_phan_tram)) / Decimal('100')
        tong_tien = Decimal(str(p_val)) * (Decimal('1') + x_dec)**2
        tong_tien_str = str(tong_tien.normalize()).replace('.', ',')
        x_dec_str = str(x_dec).replace('.', ',')
        mot_cong_x_str = str(Decimal('1') + x_dec).replace('.', ',')
        
        noidungcauhoi = ('''Cô Lan gửi số tiền gốc ban đầu là $P$ (triệu đồng) vào ngân hàng theo hình thức lãi kép với lãi suất $x\\text{/năm}$ (nghĩa là tiền lãi của năm thứ nhất được nhập vào gốc để tính lãi cho năm thứ hai). \\
a) Viết biểu thức biểu thị tổng số tiền cả gốc lẫn lãi $T$ mà cô Lan nhận được sau $2$ năm theo $P$ và $x$, sau đó phân tích biểu thức $T$ thành nhân tử. \\\\
b) Biết số tiền gốc ban đầu là $P = %s\\text{ triệu đồng}$ và sau $2$ năm cô Lan nhận được tổng cộng $%s\\text{ triệu đồng}$. Hãy tính lãi suất $x\\text{/năm}$ của ngân hàng (viết dưới dạng phần trăm).'''
                         % (p_val, tong_tien_str))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Sau năm thứ nhất, tổng số tiền cô Lan có là $P + Px = P(1 + x)$ (triệu đồng).\\\\
Sau năm thứ hai, tổng số tiền cả gốc lẫn lãi cô Lan nhận được là:
\\begin{align*}
T &= P(1 + x) + P(1 + x)x \\\\
&= P + 2Px + Px^2 \\\\
&= P(1 + 2x + x^2) = P(1 + x)^2\\text{ (triệu đồng)}.
\\end{align*}
\\item Thay $P = %s$ và $T = %s$ vào công thức trên, ta được:
\\begin{align*}
%s(1 + x)^2 &= %s \\\\
(1 + x)^2 &= %s \\\\
(1 + x)^2 - (%s)^2 &= 0 \\\\
(1 + x - %s)(1 + x + %s) &= 0.
\\end{align*}
Vì lãi suất $x > 0$ nên $1 + x + %s > 0$, suy ra $1 + x - %s = 0 \\Rightarrow x = %s = %s\\%%$.\\\\
Vậy lãi suất của ngân hàng là $%s\\%%\\text{/năm}$.
\\end{enumEX}''' % (p_val, tong_tien_str, p_val, tong_tien_str,
                      str((Decimal('1') + x_dec)**2).replace('.', ','),
                      mot_cong_x_str, mot_cong_x_str, mot_cong_x_str,
                      mot_cong_x_str, mot_cong_x_str, x_dec_str, lai_phan_tram, lai_phan_tram))

    # Xuất câu hỏi và lời giải tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
