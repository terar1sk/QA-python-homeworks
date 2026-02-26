import logging
import xml.etree.ElementTree as ET
from pathlib import Path


def find_incoming_by_group_number(group_number: str) -> str:
    xml_path = Path("lesson_16/task_3_XML/work_with_xml/groups.xml")

    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall("group"):
        num = group.findtext("number")
        if num == str(group_number):
            incoming = group.findtext("timingExbytes/incoming")
            if incoming is None:
                raise ValueError(f"Группа {group_number} найдена, но timingExbytes/incoming отсутствует")
            return incoming
    raise ValueError(f"Группа с number={group_number} не найдена")


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    logger = logging.getLogger("groups_xml")
    group_number = "0"
    incoming = find_incoming_by_group_number(group_number)
    logger.info("group/number=%s -> timingExbytes/incoming=%s", group_number, incoming)


if __name__ == "__main__":
    main()
