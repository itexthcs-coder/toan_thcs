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

def bt_dang6_p2_b4_c5_hh9(self):
    def fmt_num(val):
        if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
            return str(int(val))
        s = ("%.6f" % val).rstrip("0").rstrip(".")
        return s.replace(".", ",")

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 6: Tính chất hai tiếp tuyến cắt nhau của nửa đường tròn
        R = random.choice([3, 4, 5, 6, 7, 8])
        diam = 2 * R
        R_sq = R * R
        R_sq_sai = 2 * R * R

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (A) at (-2,0);\n"
            "\\coordinate (B) at (2,0);\n"
            "\\coordinate (C) at (-2,1.2);\n"
            "\\coordinate (D) at (2,3.333);\n"
            "\\coordinate (M) at (-0.941,1.765);\n"
            "\\draw[line width=1pt] (2,0) arc (0:180:2);\n"
            "\\draw[line width=1pt] (A)--(B);\n"
            "\\draw[line width=1pt] (-2,0)--(-2,3.8) node[left] {$x$};\n"
            "\\draw[line width=1pt] (2,0)--(2,3.8) node[right] {$y$};\n"
            "\\draw[line width=1pt] (C)--(D);\n"
            "\\draw[line width=1pt] (O)--(C) (O)--(D);\n"
            "\\draw[line width=1pt, dashed] (O)--(M);\n"
            "\\draw[line width=1pt] (-2,0.2)--(-1.8,0.2)--(-1.8,0);\n"
            "\\draw[line width=1pt] (2,0.2)--(1.8,0.2)--(1.8,0);\n"
            "\\fill (O) circle (1pt) node[below] {$O$};\n"
            "\\fill (A) circle (1pt) node[below left] {$A$};\n"
            "\\fill (B) circle (1pt) node[below right] {$B$};\n"
            "\\fill (C) circle (1pt) node[left] {$C$};\n"
            "\\fill (D) circle (1pt) node[right] {$D$};\n"
            "\\fill (M) circle (1pt) node[above] {$M$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho nửa đường tròn tâm $O$ đường kính $AB = %s\\text{ cm}$ (với bán kính $R = %s\\text{ cm}$). Kẻ hai tiếp tuyến $Ax$, $By$ cùng phía với nửa đường tròn. Qua điểm $M$ thuộc nửa đường tròn ($M \\neq A$, $M \\neq B$), kẻ tiếp tuyến thứ ba cắt $Ax$ tại $C$ và cắt $By$ tại $D$.\n%s'''
            % (fmt_num(diam), fmt_num(R), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Tổng độ dài $AC + BD$ luôn bằng độ dài đoạn thẳng $CD$'
        nb_da_1_s = 'Tổng độ dài $AC + BD$ luôn bằng đường kính $AB = %s\\text{ cm}$' % (fmt_num(diam))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Theo tính chất hai tiếp tuyến cắt nhau của nửa đường tròn $(O)$, ta có $AC = CM$ (hai tiếp tuyến tại $A$ và $M$ cắt nhau tại $C$) và $BD = DM$ (hai tiếp tuyến tại $B$ và $M$ cắt nhau tại $D$). \\\\ Do điểm $M$ nằm giữa $C$ và $D$ nên $AC + BD = CM + DM = CD$.'''
        )
        loigiai_nb_1_s = (
            '''Sai. Theo tính chất hai tiếp tuyến cắt nhau, ta có $AC = CM$ và $BD = DM$, suy ra $AC + BD = CM + DM = CD$ (thay đổi theo vị trí của $M$, không luôn bằng $AB$).'''
        )

        # Thông hiểu
        th_da_1_d = '\\True Góc $\\widehat{COD}$ luôn là góc vuông với mọi vị trí của điểm $M$ trên nửa đường tròn'
        th_da_1_s = 'Góc $\\widehat{COD}$ luôn là góc nhọn bằng $60^\\circ$ với mọi vị trí của điểm $M$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Theo tính chất hai tiếp tuyến cắt nhau, $OC$ là tia phân giác của góc $\\widehat{AOM}$ và $OD$ là tia phân giác của góc $\\widehat{BOM}$. \\\\ Vì $\\widehat{AOM}$ và $\\widehat{BOM}$ là hai góc kề bù nên $\\widehat{COD} = \\widehat{COM} + \\widehat{DOM} = \\frac{1}{2}(\\widehat{AOM} + \\widehat{BOM}) = \\frac{1}{2} \\cdot 180^\\circ = 90^\\circ$.'''
        )
        loigiai_th_1_s = (
            '''Sai. Vì $OC$ và $OD$ lần lượt là hai tia phân giác của hai góc kề bù $\\widehat{AOM}$ và $\\widehat{BOM}$ nên $\\widehat{COD} = \\frac{1}{2} \\cdot 180^\\circ = 90^\\circ$ (là góc vuông, không phải góc $60^\\circ$).'''
        )

        # Vận dụng
        vd_da_1_d = '\\True Tích $AC \\cdot BD$ không phụ thuộc vào vị trí điểm $M$ và luôn bằng $%s\\text{ cm}^2$' % (fmt_num(R_sq))
        vd_da_1_s = 'Tích $AC \\cdot BD$ không phụ thuộc vào vị trí điểm $M$ và luôn bằng $%s\\text{ cm}^2$' % (fmt_num(R_sq_sai))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Vì $CD$ tiếp xúc với nửa đường tròn $(O)$ tại $M$ nên $OM \\perp CD$ và $OM = R = %s\\text{ cm}$. \\\\ Trong tam giác $COD$ vuông tại $O$, ta có $\\widehat{COM} + \\widehat{DOM} = 90^\\circ$ và $\\widehat{COM} + \\widehat{OCM} = 90^\\circ$ nên $\\widehat{OCM} = \\widehat{DOM}$, suy ra tam giác $OMC$ đồng dạng với tam giác $DMO$ (g.g). \\\\ Do đó $\\frac{CM}{OM} = \\frac{OM}{DM} \\Rightarrow CM \\cdot DM = OM^2 = R^2 = %s^2 = %s\\text{ cm}^2$. \\\\ Mà $AC = CM$ và $BD = DM$ nên $AC \\cdot BD = CM \\cdot DM = %s\\text{ cm}^2$.'''
            % (fmt_num(R), fmt_num(R), fmt_num(R_sq), fmt_num(R_sq))
        )
        loigiai_vd_1_s = (
            '''Sai. Trong tam giác $COD$ vuông tại $O$ với đường cao $OM = R = %s\\text{ cm}$, ta có $AC \\cdot BD = CM \\cdot DM = OM^2 = %s^2 = %s\\text{ cm}^2$ (khác $%s\\text{ cm}^2$).'''
            % (fmt_num(R), fmt_num(R), fmt_num(R_sq), fmt_num(R_sq_sai))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Đường tròn đường kính $CD$ luôn tiếp xúc với đường thẳng $AB$ tại tâm $O$'
        vdc_da_1_s = 'Đường tròn đường kính $CD$ luôn cắt đường thẳng $AB$ tại hai điểm phân biệt'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Gọi $I$ là trung điểm của $CD$, khi đó $I$ là tâm đường tròn đường kính $CD$ có bán kính $R_1 = \\frac{CD}{2}$. \\\\ Vì $Ax \\perp AB$ và $By \\perp AB$ nên $AC // BD$, tứ giác $ABDC$ là hình thang vuông có $IO$ là đường trung bình, suy ra $IO // AC$ nên $IO \\perp AB$ tại $O$. \\\\ Hơn nữa, trong tam giác vuông $COD$, đường trung tuyến ứng với cạnh huyền $IO = \\frac{CD}{2} = R_1$. Vì $IO \\perp AB$ tại $O$ và $IO = R_1$ nên đường tròn đường kính $CD$ tiếp xúc với $AB$ tại $O$.'''
        )
        loigiai_vdc_1_s = (
            '''Sai. Gọi $I$ là trung điểm của $CD$. Vì $IO$ là đường trung bình của hình thang vuông $ABDC$ nên $IO \\perp AB$ tại $O$, đồng thời trong tam giác vuông $COD$ thì $IO = \\frac{CD}{2}$ bằng bán kính đường tròn đường kính $CD$. Do đó đường tròn đường kính $CD$ tiếp xúc với $AB$ tại $O$, không cắt $AB$ tại hai điểm.'''
        )

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)

            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            true_count = count_true_answers(answers)
            if 1 <= true_count <= 3:
                break

        loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s
        loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s
        loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s
        loigiai_vdc_1 = loigiai_vdc_1_d if vdc_da_1 == vdc_da_1_d else loigiai_vdc_1_s

        list_nb_1 = [nb_da_1]
        list_th_1 = [th_da_1]
        list_vd_1 = [vd_da_1]
        list_vdc_1 = [vdc_da_1]

        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

        combined_nb = list(zip(list_nb_1, list_nb_2))
        combined_th = list(zip(list_th_1, list_th_2))
        combined_vd = list(zip(list_vd_1, list_vd_2))
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))

        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu trắc nghiệm đúng sai
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
