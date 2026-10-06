from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side
)
from openpyxl.utils import get_column_letter


# --- Цветовая схема ---
COLOR_HEADER_BG = "28426A"       # тёмно-синий
COLOR_HEADER_FG = "FFFFFF"       # белый текст
COLOR_CARD_BG = "EAF0F9"         # светло-голубой для карточек
COLOR_CARD_VALUE = "3C78C8"      # акцентный синий для цифр
COLOR_TABLE_HEADER = "28426A"    # шапка таблицы
COLOR_TABLE_ROW_ALT = "F4F7FB"   # чередование строк
COLOR_TOTAL_BG = "D6E1F2"        # строка ИТОГО
COLOR_BORDER = "C8D2E0"          # цвет границ
COLOR_MUTED = "7A869A"           # приглушённый серый


def generate_excel(results: dict, output_path: str = "report.xlsx"):
    metrics = results["metrics"]
    managers = results["managers"]
    period = results["period"]
    metric_names = list(metrics.keys())

    wb = Workbook()
    ws = wb.active
    ws.title = "Отчёт"
    ws.sheet_view.showGridLines = False

    # --- Общие стили ---
    thin = Side(style="thin", color=COLOR_BORDER)
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    def set_cell(cell, value=None, font=None, fill=None, align=None, border_=None):
        if value is not None:
            cell.value = value
        if font:
            cell.font = font
        if fill:
            cell.fill = PatternFill("solid", fgColor=fill)
        if align:
            cell.alignment = align
        if border_:
            cell.border = border_

    # ============================================================
    # 1. ЗАГОЛОВОК
    # ============================================================
    total_cols = 1 + len(metric_names)   # Менеджер + метрики
    last_col_letter = get_column_letter(total_cols)

    ws.merge_cells(f"A1:{last_col_letter}1")
    set_cell(
        ws["A1"],
        "ОТЧЁТ ПО СДЕЛКАМ",
        font=Font(name="Calibri", size=20, bold=True, color=COLOR_HEADER_FG),
        fill=COLOR_HEADER_BG,
        align=Alignment(horizontal="left", vertical="center", indent=1),
    )
    ws.row_dimensions[1].height = 40

    ws.merge_cells(f"A2:{last_col_letter}2")
    set_cell(
        ws["A2"],
        f"Период: {period}",
        font=Font(name="Calibri", size=12, italic=True, color=COLOR_MUTED),
        align=Alignment(horizontal="left", vertical="center", indent=1),
    )
    ws.row_dimensions[2].height = 22

    # Пустая строка-разделитель
    ws.row_dimensions[3].height = 10

    # ============================================================
    # 2. КАРТОЧКИ С ИТОГО (каждая метрика — две строки: название + цифра)
    # ============================================================
    row_label = 4
    row_value = 5

    # Первая колонка карточек пустая (отступ) — метрики начинаются со 2-й
    for i, metric_name in enumerate(metric_names):
        col = i + 2   # начинаем с B
        letter = get_column_letter(col)

        # Название метрики
        set_cell(
            ws.cell(row=row_label, column=col),
            metric_name,
            font=Font(name="Calibri", size=11, bold=True, color=COLOR_HEADER_BG),
            fill=COLOR_CARD_BG,
            align=Alignment(horizontal="center", vertical="center"),
            border_=border,
        )

        # Значение
        set_cell(
            ws.cell(row=row_value, column=col),
            metrics[metric_name]["ИТОГО"],
            font=Font(name="Calibri", size=22, bold=True, color=COLOR_CARD_VALUE),
            fill=COLOR_CARD_BG,
            align=Alignment(horizontal="center", vertical="center"),
            border_=border,
        )

    ws.row_dimensions[row_label].height = 28
    ws.row_dimensions[row_value].height = 42

    # Пустая строка
    ws.row_dimensions[6].height = 12

    # ============================================================
    # 3. ТАБЛИЦА ПО МЕНЕДЖЕРАМ
    # ============================================================
    header_row = 7

    # Шапка таблицы
    set_cell(
        ws.cell(row=header_row, column=1),
        "Менеджер",
        font=Font(name="Calibri", size=12, bold=True, color=COLOR_HEADER_FG),
        fill=COLOR_TABLE_HEADER,
        align=Alignment(horizontal="left", vertical="center", indent=1),
        border_=border,
    )
    for i, metric_name in enumerate(metric_names):
        set_cell(
            ws.cell(row=header_row, column=i + 2),
            metric_name,
            font=Font(name="Calibri", size=12, bold=True, color=COLOR_HEADER_FG),
            fill=COLOR_TABLE_HEADER,
            align=Alignment(horizontal="center", vertical="center"),
            border_=border,
        )
    ws.row_dimensions[header_row].height = 30

    # Строки менеджеров
    for idx, manager in enumerate(managers):
        row = header_row + 1 + idx
        row_fill = COLOR_TABLE_ROW_ALT if idx % 2 == 0 else None

        set_cell(
            ws.cell(row=row, column=1),
            manager,
            font=Font(name="Calibri", size=11, color="333333"),
            fill=row_fill,
            align=Alignment(horizontal="left", vertical="center", indent=1),
            border_=border,
        )

        for i, metric_name in enumerate(metric_names):
            value = metrics[metric_name]["по_менеджерам"].get(manager, 0)
            set_cell(
                ws.cell(row=row, column=i + 2),
                value,
                font=Font(name="Calibri", size=11, color="333333"),
                fill=row_fill,
                align=Alignment(horizontal="center", vertical="center"),
                border_=border,
            )
        ws.row_dimensions[row].height = 22

    # Строка ИТОГО
    total_row = header_row + 1 + len(managers)
    set_cell(
        ws.cell(row=total_row, column=1),
        "ИТОГО",
        font=Font(name="Calibri", size=12, bold=True, color=COLOR_HEADER_BG),
        fill=COLOR_TOTAL_BG,
        align=Alignment(horizontal="left", vertical="center", indent=1),
        border_=border,
    )
    for i, metric_name in enumerate(metric_names):
        set_cell(
            ws.cell(row=total_row, column=i + 2),
            metrics[metric_name]["ИТОГО"],
            font=Font(name="Calibri", size=12, bold=True, color=COLOR_HEADER_BG),
            fill=COLOR_TOTAL_BG,
            align=Alignment(horizontal="center", vertical="center"),
            border_=border,
        )
    ws.row_dimensions[total_row].height = 26

    # ============================================================
    # 4. ШИРИНА КОЛОНОК
    # ============================================================
    ws.column_dimensions["A"].width = 30
    for i in range(len(metric_names)):
        col_letter = get_column_letter(i + 2)
        ws.column_dimensions[col_letter].width = 16

    # Скрываем первую колонку карточек? Нет — оставляем пустой отступ в A
    # (она уже широкая из-за таблицы, что визуально даёт отступ)

    # ============================================================
    # 5. ФРИЗ ПАНЕЛИ (шапка всегда видна)
    # ============================================================
    ws.freeze_panes = f"A{header_row + 1}"

    # Сохраняем
    wb.save(output_path)
    print(f"Excel-отчёт сохранён: {output_path}")