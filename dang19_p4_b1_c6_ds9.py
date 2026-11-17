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


def bt_dang19_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_dec = random.choice([Decimal('0.005'), Decimal('0.006'), Decimal('0.008')])
        v1 = 50
        v2 = 100
        d1 = a_dec * Decimal(v1**2)
        d2 = a_dec * Decimal(v2**2)
        
        v_obs = random.choice([60, 70, 80, 90])
        d_obs = a_dec * Decimal(v_obs**2)
        
        a_str = str(a_dec).replace('.', ',')
        d1_str = str(d1).rstrip('0').rstrip('.').replace('.', ',')
        d2_str = str(d2).rstrip('0').rstrip('.').replace('.', ',')
        d_obs_str = str(d_obs).rstrip('0').rstrip('.').replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Khi một chiếc ô tô đang chạy với vận tốc $v$ (km/h) trên mặt đường khô ráo và người lái đạp phanh gấp, quãng đường phanh $d$ (mét) kể từ lúc đạp phanh đến khi xe dừng hẳn được ước tính theo công thức $d = %sv^2$. \\\\
a) Hoàn thành bảng giá trị sau và nhận xét tỷ lệ tăng của quãng đường phanh khi vận tốc tăng gấp đôi từ $50$ km/h lên $100$ km/h:
\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Vận tốc $v$ (km/h) & $50$ & $100$ \\\\
\\hline
Quãng đường phanh $d$ (m) & ? & ? \\\\
\\hline
\\end{tabular}
\\end{center}
b) Nếu phía trước có chướng ngại vật bất ngờ xuất hiện ở khoảng cách $%s$ m, vận tốc tối đa của xe lúc bắt đầu đạp phanh phải là bao nhiêu km/h để xe kịp dừng lại trước khi va chạm?'''
                         %(a_str, d_obs_str
                         ))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thay lần lượt $v = 50$ và $v = 100$ vào công thức $d = %sv^2$, ta được: \\\\
- Với $v = 50$ km/h: $d = %s \\cdot 50^2 = %s \\cdot 2500 = %s$ (m). \\\\
- Với $v = 100$ km/h: $d = %s \\cdot 100^2 = %s \\cdot 10000 = %s$ (m). \\\\
Ta có bảng giá trị hoàn chỉnh:
\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Vận tốc $v$ (km/h) & $50$ & $100$ \\\\
\\hline
Quãng đường phanh $d$ (m) & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Nhận xét: Khi vận tốc tăng gấp đôi (từ $50$ km/h lên $100$ km/h), quãng đường phanh tăng gấp $4$ lần (vì $\\frac{%s}{%s} = 4$).
\\item Để xe kịp dừng lại trước khi va chạm với chướng ngại vật ở khoảng cách $%s$ m, quãng đường phanh $d$ phải thỏa mãn $d \\le %s$: \\\\
$%sv^2 \\le %s$ \\\\
$v^2 \\le \\frac{%s}{%s} = %s$ \\\\
Vì $v > 0$ nên $v \\le \\sqrt{%s} = %s$ (km/h). \\\\
Vậy vận tốc tối đa của xe lúc bắt đầu đạp phanh là $%s$ km/h.
\\end{enumEX}'''
                   %(a_str,
                     a_str, a_str, d1_str,
                     a_str, a_str, d2_str,
                     d1_str, d2_str,
                     d2_str, d1_str,
                     d_obs_str, d_obs_str,
                     a_str, d_obs_str,
                     d_obs_str, a_str, latex(v_obs**2),
                     latex(v_obs**2), latex(v_obs),
                     latex(v_obs)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
