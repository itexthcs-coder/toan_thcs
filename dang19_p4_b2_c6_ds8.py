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


def bt_dang19_p4_b2_c6_ds8(self):
    # Dạng 19: Năng suất & Quản lí sản xuất - Bài toán hợp đồng may đồng phục học sinh
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        tong_bo = 1500
        ngay_dau = 6
        tang_them = 25
        x_val = 100
        con_lai = tong_bo - ngay_dau * x_val
        ngay_sau = Rational(con_lai, x_val + tang_them)
        tong_ngay = ngay_dau + ngay_sau
        han_hd = 15

        noidungcauhoi = ('Một xưởng may kí hợp đồng sản xuất $%s$ bộ đồng phục học sinh trong thời hạn $%s$ ngày. Trong $%s$ ngày đầu, mỗi ngày xưởng may được $x$ bộ đồng phục ($x \\in \\mathbb{N}^*, x < 250$). Nhờ bổ sung thêm máy may công nghiệp, trong những ngày còn lại mỗi ngày xưởng may được nhiều hơn ban đầu $%s$ bộ đồng phục.\\\n'
                         'a) Viết phân thức biểu thị số ngày xưởng hoàn thành số bộ đồng phục còn lại sau $%s$ ngày đầu.\\\n'
                         'b) Tính tổng thời gian xưởng hoàn thành toàn bộ hợp đồng khi $x = %s$.\\\n'
                         'c) Với năng suất ban đầu $x = %s$ bộ/ngày, xưởng có hoàn thành hợp đồng đúng hạn hay không? Vì sao?'
                         % (tong_bo, han_hd, ngay_dau, tang_them, ngay_dau, x_val, x_val))

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Trong $%s$ ngày đầu, xưởng may được $%sx$ bộ đồng phục nên số bộ đồng phục còn lại là $(%s - %sx)$ bộ.\\\n'
                   'Năng suất trong những ngày còn lại là $(x + %s)$ bộ/ngày.\\\n'
                   'Do đó phân thức biểu thị số ngày xưởng hoàn thành số bộ đồng phục còn lại là $\\dfrac{%s - %sx}{x + %s}$ (ngày).\n'
                   '\\item Thay $x = %s$ vào phân thức trên, số ngày hoàn thành phần còn lại là:\\\n'
                   '$\\dfrac{%s - %s \\cdot %s}{%s + %s} = \\dfrac{%s}{%s} = %s$ (ngày).\\\n'
                   'Tổng thời gian xưởng hoàn thành toàn bộ hợp đồng là $%s + %s = %s$ (ngày).\n'
                   '\\item Vì $%s < %s$ nên xưởng hoàn thành hợp đồng sớm hơn thời hạn $%s$ ngày (đảm bảo hoàn thành đúng hạn).\n'
                   '\\end{enumEX}'
                   % (ngay_dau, ngay_dau, tong_bo, ngay_dau, tang_them, tong_bo, ngay_dau, tang_them,
                      x_val, tong_bo, ngay_dau, x_val, x_val, tang_them, con_lai, x_val + tang_them, latex(ngay_sau),
                      ngay_dau, latex(ngay_sau), latex(tong_ngay),
                      latex(tong_ngay), han_hd, latex(han_hd - tong_ngay)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
