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


def bt_dang15_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        w = random.choice([1.2, 1.22, 1.25])
        w_str = str(w).replace('.', ',')
        k = random.choice([4, 5, 6, 7, 8])
        so_lan = k - 1
        val = 2 * 3.14 * so_lan * w
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một đường chạy điền kinh gồm hai đoạn thẳng song song dài $100\\text{ m}$ và hai đầu là hai nửa đường tròn có cùng tâm. Làn chạy số 1 (trong cùng) có bán kính mép trong là $36,5\\text{ m}$, mỗi làn chạy rộng $%s\\text{ m}$. Để các vận động viên chạy hết đúng một vòng sân (tính theo mép trong của mỗi làn) đều đi quãng đường như nhau, vạch xuất phát ở làn chạy số $%d$ phải đặt cao hơn vạch xuất phát ở làn chạy số 1 bao nhiêu mét (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần mười)?
\\begin{center}
\\begin{tikzpicture}[scale=0.75]
\\draw (-1.8,1.2) -- (1.8,1.2) arc (90:-90:1.2) -- (-1.8,-1.2) arc (270:90:1.2);
\\draw (-1.8,0.8) -- (1.8,0.8) arc (90:-90:0.8) -- (-1.8,-0.8) arc (270:90:0.8);
\\draw[dashed] (-1.8,1.2) -- (-1.8,-1.2);
\\draw[dashed] (1.8,1.2) -- (1.8,-1.2);
\\node at (0,0) {$100\\text{ m}$};
\\end{tikzpicture}
\\end{center}''' % (w_str, k))

        # Nội dung lời giải
        loigiai = ('''Gọi $R_1 = 36,5\\text{ m}$ là bán kính mép trong của làn chạy số 1 và $R_%d$ là bán kính mép trong của làn chạy số $%d$. \\\\
Vì mỗi làn rộng $%s\\text{ m}$ nên mép trong làn số $%d$ cách mép trong làn số 1 một khoảng là:
$$R_%d - R_1 = (%d - 1) \\cdot %s = %d \\cdot %s\\text{ (m)}.$$
Hai nửa đường tròn ở hai đầu sân của mỗi làn hợp lại thành một đường tròn hoàn chỉnh. Vì phần đường thẳng ở tất cả các làn đều dài $100\\text{ m}$ nên độ chênh lệch quãng đường một vòng chạy giữa làn số $%d$ và làn số 1 chính là hiệu chu vi hai đường tròn:
$$\\Delta C = 2\\pi R_%d - 2\\pi R_1 = 2\\pi(R_%d - R_1) \\approx 2 \\cdot 3,14 \\cdot %d \\cdot %s \\approx %s\\text{ (m)}.$$''' % (
            k, k, w_str, k, k, k, w_str, so_lan, w_str, k, k, k, so_lan, w_str, kq_str))

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
