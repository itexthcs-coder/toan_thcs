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


def bt_dang7_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.randint(2, 10)
        a = 2 * k
        ans = k ** 2
        kq_str = str(ans)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông cân tại $A$ có cạnh góc vuông $AB = %d\\text{ cm}$. Vẽ nửa đường tròn đường kính $BC$ đi qua $A$ và vẽ nửa đường tròn đường kính $AB$ nằm về phía ngoài tam giác $ABC$. Tính diện tích phần hình phẳng giới hạn bởi hai nửa đường tròn đó (hình trăng khuyết trên cạnh $AB$) theo đơn vị $\\text{cm}^2$.
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\fill[yellow!35] (0,2) arc (90:270:1) arc (225:135:1.4142) -- cycle;
\\draw (0,0) -- (0,2) -- (2,0) -- cycle;
\\draw (2,0) arc (315:135:1.4142);
\\draw (0,2) arc (90:270:1);
\\draw (0,0.2) -- (0.2,0.2) -- (0.2,0);
\\node[below left] at (0,0) {$A$};
\\node[above] at (0,2) {$B$};
\\node[right] at (2,0) {$C$};
\\end{tikzpicture}
\\end{center}''' % (a))

        # Nội dung lời giải
        loigiai = ('''Tam giác $ABC$ vuông cân tại $A$ có $AB = AC = %d\\text{ cm}$ nên $BC = AB\\sqrt{2} = %d\\sqrt{2}\\text{ (cm)}$. \\\\
Nửa đường tròn đường kính $BC$ có tâm $O$ là trung điểm $BC$, bán kính $R = \\dfrac{BC}{2} = %d\\sqrt{2}\\text{ (cm)}$ và cung nhỏ $AB$ có số đo $90^\\circ$. \\\\
Diện tích hình viên phân giới hạn bởi dây $AB$ và cung nhỏ $AB$ của đường tròn $(O; R)$ là:
$$S_{\\text{vp}} = \\dfrac{90}{360}\\pi (%d\\sqrt{2})^2 - \\dfrac{1}{2}(%d\\sqrt{2})^2 = %s\\pi - %d\\text{ (cm}^2\\text{)}.$$
Nửa hình tròn đường kính $AB$ có bán kính $r = \\dfrac{AB}{2} = %d\\text{ cm}$, diện tích là:
$$S_{\\text{nửa}} = \\dfrac{1}{2}\\pi \\cdot %d^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
Diện tích hình trăng khuyết trên cạnh $AB$ là:
$$S = S_{\\text{nửa}} - S_{\\text{vp}} = %s\\pi - \\left(%s\\pi - %d\\right) = %s\\text{ (cm}^2\\text{)}.$$''' % (
            a, a, k, k, k, latex(Rational(k ** 2, 2)), ans, k, k, latex(Rational(k ** 2, 2)), latex(Rational(k ** 2, 2)), latex(Rational(k ** 2, 2)), ans, kq_str))

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
