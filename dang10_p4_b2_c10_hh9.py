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


def bt_dang10_p4_b2_c10_hh9(self):
    # 3 quả cầu bán kính R tiếp xúc đôi một trên mặt phẳng ngang, quả thứ 4 đặt lên trên tiếp xúc cả 3 quả dưới.
    # 4 tâm tạo thành tứ diện đều cạnh a = 2R. Chiều cao tứ diện đều: h_td = a * sqrt(6)/3 = 2R * sqrt(6)/3.
    # Chiều cao tổng cộng của chồng bóng: H = R + h_td + R = 2R * (1 + sqrt(6)/3).
    R = randint(3, 10)
    a = 2 * R
    H_round = Decimal(str(2 * R * (1 + math.sqrt(6) / 3))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    H_str = str(H_round).replace('.', ',')

    noidungcauhoi = ('''Đặt ba quả cầu đặc giống hệt nhau, mỗi quả có bán kính $R = %s\\text{ cm}$, lên một mặt phẳng nằm ngang sao cho chúng tiếp xúc ngoài đôi một với nhau. Sau đó đặt quả cầu thứ tư có cùng bán kính $R = %s\\text{ cm}$ lên trên sao cho nó tiếp xúc với cả ba quả cầu bên dưới.\\\na) Chứng minh rằng tâm của bốn quả cầu tạo thành một hình tứ diện đều và tính độ dài cạnh của tứ diện đều đó.\\\nb) Tính chiều cao của hình tứ diện đều tạo bởi bốn tâm.\\\nc) Tính khoảng cách từ điểm cao nhất của quả cầu thứ tư xuống mặt phẳng nằm ngang (làm tròn kết quả đến hàng phần trăm của $\\text{cm}$).'''
                     % (R, R))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $O_1, O_2, O_3$ là tâm của ba quả cầu nằm dưới và $O_4$ là tâm của quả cầu nằm trên.\\\nVì bốn quả cầu có cùng bán kính $R = %s\\text{ cm}$ và tiếp xúc ngoài đôi một với nhau nên khoảng cách giữa hai tâm bất kì đều bằng $2R = %s\\text{ cm}$.\\\nDo đó $O_1O_2 = O_2O_3 = O_3O_1 = O_4O_1 = O_4O_2 = O_4O_3 = %s\\text{ cm}$, suy ra $O_4.O_1O_2O_3$ là hình tứ diện đều cạnh $a = %s\\text{ cm}$.
\\item Gọi $G$ là trọng tâm tam giác đều $O_1O_2O_3$, ta có $O_4G \\perp (O_1O_2O_3)$ và $O_1G = \\dfrac{a\\sqrt{3}}{3} = \\dfrac{%s\\sqrt{3}}{3}\\text{ (cm)}$.\\\nChiều cao của hình tứ diện đều là:
$$h = O_4G = \\sqrt{O_4O_1^2 - O_1G^2} = \\sqrt{%s^2 - \\left(\\dfrac{%s\\sqrt{3}}{3}\\right)^2} = \\dfrac{%s\\sqrt{6}}{3}\\text{ (cm)}.$$
\\item Mặt phẳng $(O_1O_2O_3)$ song song và cách mặt phẳng nằm ngang một khoảng bằng bán kính $R = %s\\text{ cm}$. Điểm cao nhất của quả cầu thứ tư cao hơn tâm $O_4$ một khoảng bằng $R = %s\\text{ cm}$.\\\nVậy chiều cao tổng cộng từ điểm cao nhất xuống mặt phẳng nằm ngang là:
$$H = R + h + R = 2R + \\dfrac{%s\\sqrt{6}}{3} = %s + \\dfrac{%s\\sqrt{6}}{3} \\approx %s\\text{ (cm)}.$$
\\end{enumEX}'''
               % (R, a, a, a, a, a, a, a, R, R, a, a, a, H_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
