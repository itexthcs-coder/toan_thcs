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


def bt_dang18_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    r1 = random.choice([12, 15, 18])
    r2 = r1 + random.choice([8, 10, 12])
    o1o2 = r2 - r1
    khe_ho = 2 * (r2 - r1)
    r1_moi = r1 - 3
    dt_rong = r2**2 - r1**2

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O2) at (0,0);
\\coordinate (O1) at (0,-1);
\\coordinate (T) at (0,-2.5);
\\draw[line width=1pt] (O2) circle (2.5cm);
\\draw[line width=1pt] (O1) circle (1.5cm);
\\draw[line width=1pt, dashed] (0,2.5)--(T);
\\fill (O2) circle (1pt) node[right] {$O_2$};
\\fill (O1) circle (1pt) node[right] {$O_1$};
\\fill (T) circle (1pt) node[below] {$T$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Để cách nhiệt, một đường ống dẫn dầu hình trụ có tiết diện tròn $(O_1; %s\\text{ cm})$ được đặt nằm bên trong một ống bảo vệ hình trụ có tiết diện tròn $(O_2; %s\\text{ cm})$ sao cho ống dẫn dầu tựa sát lên đáy trong của ống bảo vệ (tiếp xúc trong tại điểm thấp nhất $T$).
%s""" % (fmt(r1), fmt(r2), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Tâm $O_1$ của ống dẫn dầu nằm thấp hơn tâm $O_2$ của ống bảo vệ một đoạn $%s\\text{ cm}$' % (fmt(o1o2))
    nb_da_1_s = 'Tâm $O_1$ của ống dẫn dầu nằm cao hơn tâm $O_2$ của ống bảo vệ một đoạn $%s\\text{ cm}$' % (fmt(o1o2))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì hai đường tròn tiếp xúc trong tại điểm thấp nhất $T$ nên $O_2, O_1, T$ thẳng hàng theo thứ tự đó, và $O_1O_2 = R_2 - R_1 = %s - %s = %s\\text{ cm}$. Vậy $O_1$ nằm thấp hơn $O_2$ một đoạn $%s\\text{ cm}$.""" % (fmt(r2), fmt(r1), fmt(o1o2), fmt(o1o2)))

    # Thông hiểu
    th_da_1_d = '\\True Khoảng trống lớn nhất giữa đỉnh của ống dẫn dầu và đỉnh của ống bảo vệ theo phương thẳng đứng bằng $%s\\text{ cm}$' % (fmt(khe_ho))
    th_da_1_s = 'Khoảng trống lớn nhất giữa đỉnh của ống dẫn dầu và đỉnh của ống bảo vệ theo phương thẳng đứng bằng $%s\\text{ cm}$' % (fmt(o1o2))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Khoảng trống theo phương thẳng đứng ở đỉnh trên bằng hiệu đường kính của hai ống: $2R_2 - 2R_1 = 2(%s - %s) = %s\\text{ cm}$.""" % (fmt(r2), fmt(r1), fmt(khe_ho)))

    # Vận dụng
    vd_da_1_d = '\\True Nếu dùng một ống dẫn dầu khác cùng tâm $O_1$ nhưng có bán kính $%s\\text{ cm}$ thì ống này nằm hoàn toàn bên trong ống bảo vệ và không chạm vào thành ống bảo vệ' % (fmt(r1_moi))
    vd_da_1_s = 'Nếu dùng một ống dẫn dầu khác cùng tâm $O_1$ nhưng có bán kính $%s\\text{ cm}$ thì ống này vẫn chạm vào đáy ống bảo vệ tại $T$' % (fmt(r1_moi))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Với bán kính mới $R'_1 = %s\\text{ cm}$, ta có $R_2 - R'_1 = %s - %s = %s\\text{ cm} > O_1O_2 = %s\\text{ cm}$. Do đó đường tròn $(O_2; R_2)$ đựng đường tròn $(O_1; R'_1)$ (không có điểm chung).""" % (fmt(r1_moi), fmt(r2), fmt(r1_moi), fmt(r2 - r1_moi), fmt(o1o2)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Thiết diện phần không gian rỗng nằm giữa hai ống có diện tích bằng $%s\\pi\\text{ cm}^2$' % (fmt(dt_rong))
    vdc_da_1_s = 'Thiết diện phần không gian rỗng nằm giữa hai ống có diện tích bằng $%s\\pi\\text{ cm}^2$' % (fmt((r2 - r1)**2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Diện tích phần không gian rỗng bằng hiệu diện tích hình tròn ngoài và hình tròn trong: $S = \\pi R_2^2 - \\pi R_1^2 = \\pi(%s^2 - %s^2) = %s\\pi\\text{ cm}^2$.""" % (fmt(r2), fmt(r1), fmt(dt_rong)))

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
