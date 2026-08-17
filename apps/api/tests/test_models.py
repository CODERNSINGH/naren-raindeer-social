import pytest
from sqlalchemy.orm import Session

from apps.api.config.database import SessionLocal
from apps.api.models import Brand, Organization, User


@pytest.fixture
def db() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


def test_organization_table_name() -> None:
    assert Organization.__tablename__ == "organizations"


def test_user_table_name() -> None:
    assert User.__tablename__ == "users"


def test_brand_table_name() -> None:
    assert Brand.__tablename__ == "brands"


def test_brand_has_report_and_embedding_columns() -> None:
    assert "brand_report" in Brand.__table__.columns
    assert "report_embedding" in Brand.__table__.columns


def test_create_organization_user_brand(db: Session) -> None:
    org = Organization(name="Acme Inc")
    db.add(org)
    db.flush()

    user = User(organization_id=org.id, email="owner@acme.test", full_name="Ada Owner")
    brand = Brand(
        organization_id=org.id,
        name="Acme Brand",
        brand_report={"summary": "test report"},
        report_embedding=[0.0] * 1536,
    )
    db.add_all([user, brand])
    db.flush()

    assert user.organization_id == org.id
    assert brand.organization_id == org.id
    assert brand.brand_report == {"summary": "test report"}
    assert len(brand.report_embedding) == 1536
