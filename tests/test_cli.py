import pytest

from hiring.cli import build_parser


@pytest.mark.parametrize("argv,expected_command", [
    (["setup"], "setup"),
    (["teams"], "teams"),
    (["prep", "--name", "Jane Doe"], "prep"),
    (["index"], "index"),
    (["scorecard", "init", "--name", "Jane Doe"], "scorecard"),
    (["cv2md", "cv.pdf"], "cv2md"),
    (["dashboard"], "dashboard"),
])
def test_build_parser_recognizes_commands(argv, expected_command):
    args = build_parser().parse_args(argv)
    assert args.command == expected_command


def test_prep_defaults():
    args = build_parser().parse_args(["prep", "--name", "Jane Doe"])
    assert args.seniority == "senior"
    assert args.language is None
    assert args.force is False


def test_prep_requires_name():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["prep"])


def test_no_command_is_required():
    with pytest.raises(SystemExit):
        build_parser().parse_args([])


def test_dashboard_defaults():
    args = build_parser().parse_args(["dashboard"])
    assert args.port == 8080
    assert args.no_browser is False


def test_scorecard_mode_choices_enforced():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["scorecard", "bogus"])


def test_seniority_choices_enforced():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["prep", "--name", "Jane Doe", "--seniority", "bogus"])
