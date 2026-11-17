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


def bt_dang15_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = randint(3, 12)
        d = 2 * r
        ab_exact = r * sqrt(2)
        ab_dec = Decimal(str(float(ab_exact))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        ab_str = str(ab_dec).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một góc tường vuông góc tại $M$ ($\\widehat{xMy} = 90^\\circ$), người thợ đặt một ống nước hình trụ có đường kính ngoài $%s\\text{ cm}$ nằm áp sát vào cả hai bức tường $Mx$ và $My$ (mặt cắt ngang là đường tròn tâm $O$ tiếp xúc với $Mx$ và $My$ lần lượt tại $A$ và $B$). Để ốp một tấm che góc phẳng đi qua hai tiếp điểm $A$ và $B$ trên hai bức tường, người thợ cần cắt tấm che có chiều rộng $AB$ bằng bao nhiêu xen-ti-mét (làm tròn kết quả đến chữ số thập phân thứ hai)? \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (M) at (0,0);
            \\coordinate (A) at (0,1.6);
            \\coordinate (B) at (1.6,0);
            \\coordinate (O) at (1.6,1.6);
            \\draw[line width=1pt] (O) circle (1.6);
            \\draw[line width=1pt] (0,3.6) node[left] {$x$} -- (M) -- (3.6,0) node[below] {$y$};
            \\draw[line width=1pt] (A)--(B);
            \\draw[line width=1pt, dashed] (O)--(A) (O)--(B);
            \\fill (M) circle (1pt) node[below left] {$M$};
            \\fill (A) circle (1pt) node[left] {$A$};
            \\fill (B) circle (1pt) node[below] {$B$};
            \\fill (O) circle (1pt) node[above right] {$O$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(d)))

        # Nội dung lời giải
        loigiai = ('''Bán kính mặt cắt ngoài của ống nước là $R = \\dfrac{%s}{2} = %s\\text{ (cm)}$. \\\\
        Vì đường tròn $(O; %s\\text{ cm})$ tiếp xúc với hai bức tường $Mx$ và $My$ lần lượt tại $A$ và $B$ nên $OA \\perp Mx$ tại $A$ và $OB \\perp My$ tại $B$, hay $\\widehat{OAM} = \\widehat{OBM} = 90^\\circ$. \\\\
        Xét tứ giác $OAMB$ có $\\widehat{OAM} = \\widehat{OBM} = \\widehat{AMB} = 90^\\circ$ nên $OAMB$ là hình chữ nhật. \\\\
        Mặt khác, $OA = OB = R = %s\\text{ cm}$ nên hình chữ nhật $OAMB$ là hình vuông cạnh $%s\\text{ cm}$, suy ra $MA = MB = %s\\text{ cm}$. \\\\
        Áp dụng định lí Pythagore trong tam giác $MAB$ vuông tại $M$, chiều rộng tấm che góc là: \\\\
        $AB = \\sqrt{MA^2 + MB^2} = \\sqrt{%s^2 + %s^2} = %s\\sqrt{2} \\approx %s\\text{ (cm)}$.'''
        %(latex(d), latex(r), latex(r), latex(r), latex(r), latex(r), latex(r), latex(r), latex(r), ab_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
