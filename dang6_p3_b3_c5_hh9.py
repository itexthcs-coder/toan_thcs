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


def bt_dang6_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(2, 7)
        a = 2 * R
        val = (R ** 2) * (math.sqrt(3) - 3.14 / 2)
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho ba đường tròn có cùng bán kính $R = %d\\text{ cm}$ đôi một tiếp xúc ngoài với nhau. Tính diện tích phần mặt phẳng nằm ngoài cả ba đường tròn nhưng được giới hạn bởi ba cung tròn nối các tiếp điểm đó theo đơn vị $\\text{cm}^2$ (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\fill[green!20] (0,0) -- (2.4,0) -- (60:2.4) -- cycle;
\\fill[white] (0,0) circle (1.2);
\\fill[white] (2.4,0) circle (1.2);
\\fill[white] (60:2.4) circle (1.2);
\\draw (0,0) circle (1.2);
\\draw (2.4,0) circle (1.2);
\\draw (60:2.4) circle (1.2);
\\draw[dashed] (0,0) -- (2.4,0) -- (60:2.4) -- cycle;
\\fill (0,0) circle (1.5pt) node[below left] {$O_1$};
\\fill (2.4,0) circle (1.5pt) node[below right] {$O_2$};
\\fill (60:2.4) circle (1.5pt) node[above] {$O_3$};
\\end{tikzpicture}
\\end{center}''' % (R))

        # Nội dung lời giải
        loigiai = ('''Gọi $O_1, O_2, O_3$ là tâm của ba đường tròn. Vì ba đường tròn có cùng bán kính $R = %d\\text{ cm}$ và đôi một tiếp xúc ngoài với nhau nên $O_1O_2 = O_2O_3 = O_3O_1 = 2R = %d\\text{ (cm)}$. \\\\
Do đó $\\triangle O_1O_2O_3$ là tam giác đều cạnh $%d\\text{ cm}$, có diện tích:
$$S_{\\triangle O_1O_2O_3} = \\dfrac{%d^2\\sqrt{3}}{4} = %d\\sqrt{3}\\text{ (cm}^2\\text{)}.$$
Mỗi góc của tam giác đều bằng $60^\\circ$ nên ba hình quạt tròn nằm bên trong $\\triangle O_1O_2O_3$ có cùng bán kính $R = %d\\text{ cm}$ và góc ở tâm $60^\\circ$. Tổng diện tích của ba hình quạt tròn đó là:
$$3S_q = 3 \\cdot \\dfrac{60}{360}\\pi \\cdot %d^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
Diện tích phần mặt phẳng cần tìm là:
$$S = S_{\\triangle O_1O_2O_3} - 3S_q = %d\\sqrt{3} - %s\\pi \\approx %d\\sqrt{3} - %s \\cdot 3,14 \\approx %s\\text{ (cm}^2\\text{)}.$$''' % (
            R, a, a, a, R ** 2, R, R, latex(Rational(R ** 2, 2)), R ** 2, latex(Rational(R ** 2, 2)), R ** 2, latex(Rational(R ** 2, 2)), kq_str))

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
