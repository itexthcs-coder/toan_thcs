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


def bt_dang16_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        R = random.choice([50, 60, 70, 80])
        D = 2 * R
        h_sau = random.choice([25, 30, 35, 40])
        x_diem = random.choice([20, 30, 40])
        a = Rational(h_sau, R**2)
        y_diem = a * (x_diem**2)
        number = Decimal(float(y_diem))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một ăng-ten chảo parabol có mặt cắt qua trục đối xứng là một đường parabol $y=ax^2$ với đỉnh là tâm của đáy chảo. Biết đường kính miệng chảo là $%s\\text{ cm}$ và chiều sâu của chảo là $%s\\text{ cm}$. Khi chọn hệ trục tọa độ $Oxy$ có gốc $O$ tại đỉnh chảo và trục $Oy$ là trục đối xứng hướng lên trên, một điểm trên thành chảo cách trục đối xứng $%s\\text{ cm}$ sẽ có độ cao so với đáy chảo là bao nhiêu xăng-ti-mét? (Làm tròn kết quả đến hàng phần mười).
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.2) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.8:2.8] plot (\\x, {0.4*(\\x)^2});
\\draw[line width=1pt, dashed] (-2.8,3.136) -- (2.8,3.136);
\\coordinate (O) at (0,0);
\\coordinate (B) at (2.8,3.136);
\\coordinate (M) at (1.8,1.296);
\\coordinate (H) at (1.8,0);
\\draw[line width=1pt, dashed] (M)--(H);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (M) circle (1pt) node[right] {$M$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}'''
                         % (str(D), str(h_sau), str(x_diem)))

        # Nội dung lời giải
        loigiai = ('''Vì đường kính miệng chảo là $%s\\text{ cm}$ nên bán kính miệng chảo là $\\dfrac{%s}{2} = %s\\text{ cm}$. \\\\
Chiều sâu của chảo là $%s\\text{ cm}$ nên điểm $B$ nằm trên vành miệng chảo có tọa độ $B(%s; %s)$. \\\\
Thay tọa độ điểm $B(%s; %s)$ vào phương trình parabol $y = ax^2$, ta có: \\\\
$%s = a \\cdot %s^2 \\Leftrightarrow a = \\dfrac{%s}{%s} = %s$. \\\\
Suy ra phương trình mặt cắt parabol của chảo là $y = %s x^2$. \\\\
Điểm $M$ trên thành chảo cách trục đối xứng $Oy$ một khoảng $%s\\text{ cm}$ nên có hoành độ $|x_M| = %s$. \\\\
Độ cao của điểm $M$ so với đáy chảo chính là tung độ $y_M$: \\\\
$y_M = %s \\cdot %s^2 = %s \\approx %s\\text{ (cm)}$. \\\\
Vậy độ cao cần tìm là $%s\\text{ cm}$.'''
                   % (str(D), str(D), str(R),
                      str(h_sau), str(R), str(h_sau),
                      str(R), str(h_sau),
                      str(h_sau), str(R), str(h_sau), str(R**2), latex(a),
                      latex(a),
                      str(x_diem), str(x_diem),
                      latex(a), str(x_diem), latex(y_diem), str(kq_str),
                      str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
