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


def bt_dang12_p3_b3_c8_ds8(self):
    # Dạng 12: Bài toán kinh tế - Tính chi phí bảo hành dự kiến từ tỉ lệ lỗi thực nghiệm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_mau = random.choice([500, 800, 1000])
        k_loi = random.choice([15, 20, 24, 30])
        while (5000 * k_loi) % n_mau != 0:
            k_loi = random.choice([10, 15, 20, 24, 25, 30, 40])
        n_lo = random.choice([4000, 5000, 6000])
        while (n_lo * k_loi) % n_mau != 0:
            n_lo = random.choice([4000, 5000, 6000, 8000])
        so_loi_du_bao = (n_lo * k_loi) // n_mau
        tien_hoan_nghin = random.choice([120, 150, 180, 200])
        tong_tien_trieu = Decimal(so_loi_du_bao * tien_hoan_nghin) / Decimal(1000)
        kq = tong_tien_trieu.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).rstrip('0').rstrip('.').replace('.', ',')

        p_str = str((Decimal(k_loi) / Decimal(n_mau)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Kiểm tra ngẫu nhiên $%s$ chiếc tai nghe không dây của một hãng điện tử thấy có $%s$ chiếc bị lỗi pin. Hãng xuất bán một lô gồm $%s$ chiếc tai nghe và cam kết hoàn tiền $%s$ nghìn đồng cho mỗi chiếc bị lỗi pin. Hỏi hãng cần dự trù khoản tiền hoàn trả cho lô hàng này là bao nhiêu triệu đồng?'''
                         % (n_mau, k_loi, n_lo, tien_hoan_nghin))

        loigiai = ('''Xác suất thực nghiệm của biến cố $E$: ``Chiếc tai nghe bị lỗi pin'' là $\\dfrac{%s}{%s} = %s$.\\
Dự đoán trong lô hàng $%s$ chiếc tai nghe có khoảng $%s \\cdot %s = %s$ (chiếc) bị lỗi pin.\\
Đổi $%s$ nghìn đồng $= %s$ triệu đồng.\\
Khoản tiền hãng cần dự trù để hoàn trả là: $%s \\cdot %s = %s$ (triệu đồng).'''
                   % (k_loi, n_mau, p_str, n_lo, n_lo, p_str, so_loi_du_bao,
                      tien_hoan_nghin, str(Decimal(tien_hoan_nghin)/Decimal(1000)).rstrip('0').rstrip('.').replace('.', ','),
                      so_loi_du_bao, str(Decimal(tien_hoan_nghin)/Decimal(1000)).rstrip('0').rstrip('.').replace('.', ','), kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
