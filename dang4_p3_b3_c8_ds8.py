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


def bt_dang4_p3_b3_c8_ds8(self):
    # Dạng 4: Dự báo doanh thu/số lượng bán hàng dựa trên khảo sát thị hiếu theo nhóm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_mau = random.choice([100, 120, 150, 200])
        k_ol = random.randint(int(0.4 * n_mau), int(0.5 * n_mau))
        k_tc = random.randint(int(0.15 * n_mau), int(0.25 * n_mau))
        k_tt = n_mau - k_ol - k_tc
        he_so = random.choice([10, 15, 20, 25])
        n_khach = n_mau * he_so
        kq_int = (k_ol - k_tc) * he_so
        kq_str = str(kq_int)

        p_ol_str = str((Decimal(k_ol) / Decimal(n_mau)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')
        p_tc_str = str((Decimal(k_tc) / Decimal(n_mau)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Một quán trà sữa khảo sát ngẫu nhiên $%s$ khách hàng trong ngày khai trương, kết quả thu được như bảng sau:\\
\begin{center}
\begin{tabular}{|l|c|c|c|}
\hline
Loại đồ uống & Vị truyền thống & Vị ô long & Vị trái cây \\
\hline
Số khách chọn & $%s$ & $%s$ & $%s$ \\
\hline
\end{tabular}
\end{center}
Nếu trong tuần lễ khuyến mãi quán phục vụ $%s$ lượt khách, dự đoán lượng khách chọn vị ô long nhiều hơn lượng khách chọn vị trái cây là bao nhiêu người?'''
                         % (n_mau, k_tt, k_ol, k_tc, n_khach))

        loigiai = ('''Xác suất thực nghiệm khách chọn vị ô long là $\\dfrac{%s}{%s} = %s$.\\
Dự đoán trong $%s$ lượt khách có khoảng $%s \\cdot %s = %s$ khách chọn vị ô long.\\
Xác suất thực nghiệm khách chọn vị trái cây là $\\dfrac{%s}{%s} = %s$.\\
Dự đoán trong $%s$ lượt khách có khoảng $%s \\cdot %s = %s$ khách chọn vị trái cây.\\
Vậy lượng khách chọn vị ô long nhiều hơn lượng khách chọn vị trái cây là: $%s - %s = %s$ (người).'''
                   % (k_ol, n_mau, p_ol_str, n_khach, n_khach, p_ol_str, k_ol * he_so,
                      k_tc, n_mau, p_tc_str, n_khach, n_khach, p_tc_str, k_tc * he_so,
                      k_ol * he_so, k_tc * he_so, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
