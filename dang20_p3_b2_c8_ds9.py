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


def bt_dang20_p3_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        dk = random.choice([
            ('ít nhất là $40$ điểm', '$(S, 40); (N, 30); (N, 40)$', 3),
            ('lớn hơn $30$ điểm', '$(S, 40); (N, 30); (N, 40)$', 3),
            ('bằng $30$ điểm', '$(S, 30); (N, 20)$', 2),
            ('nhỏ hơn $30$ điểm', '$(S, 10); (S, 20); (N, 10)$', 3)
        ])
        nd_dk, chuoi_tl, so_tl = dk
        xs = Rational(so_tl, 8)
        if xs.q in [1, 2, 4]:
            kq_str = ('%g' % float(xs)).replace('.', ',')
        else:
            number = Decimal(float(xs))
            kq_str = str(number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Đồng xu $\\backslash$ Thẻ & $10$ & $20$ & $30$ & $40$ \\\\
\\hline
Sấp ($S$, $+0$) & $10$ & $20$ & $30$ & $40$ \\\\
\\hline
Ngửa ($N$, $+10$) & $20$ & $30$ & $40$ & $50$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        noidungcauhoi = ('''Một trò chơi gồm hai lượt: ở lượt $1$, người chơi tung một đồng xu cân đối; ở lượt $2$, người chơi rút ngẫu nhiên một tấm thẻ từ hộp chứa $4$ tấm thẻ ghi điểm số $10; 20; 30; 40$. Tổng điểm của người chơi bằng điểm ghi trên thẻ cộng thêm $10$ điểm nếu đồng xu xuất hiện mặt ngửa, và giữ nguyên điểm ghi trên thẻ nếu đồng xu xuất hiện mặt sấp. Tính xác suất để người chơi đạt được tổng điểm %s (làm tròn kết quả đến hàng phần trăm nếu cần).'''
                         % (nd_dk))

        loigiai = ('''Ta lập bảng tính tổng điểm tương ứng với $8$ kết quả đồng khả năng của phép thử:%s
Không gian mẫu $\\Omega$ gồm $2 \\cdot 4 = 8$ phần tử đồng khả năng.\\\\
Các kết quả để tổng điểm %s là: %s, suy ra có $%s$ kết quả thuận lợi.\\\\
Vậy xác suất cần tìm là $P = \\dfrac{%s}{8} \\approx %s$.'''
                   % (bang_mau, nd_dk, chuoi_tl, so_tl, so_tl, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
