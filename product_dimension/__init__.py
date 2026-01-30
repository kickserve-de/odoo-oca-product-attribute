# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from . import models


def create_dimension_uoms(env):
    """Create dimension UoMs if they don't exist, linked to meter"""
    meter = env.ref("uom.product_uom_meter")

    uoms_to_create = [
        {"name": "mm", "factor": 0.00100},
        {"name": "cm", "factor": 0.01000},
        {"name": "inch", "factor": 0.02540},
        {"name": "ft", "factor": 0.30480},
        {"name": "yard", "factor": 0.91440},
        {"name": "km", "factor": 1000},
    ]

    for uom_data in uoms_to_create:
        # Only create if UoM with the same name and relative_uom_id = meter does NOT exist
        existing = env["uom.uom"].search([
            ("relative_factor", "=", uom_data["factor"]),
            ("relative_uom_id", "=", meter.id)
        ], limit=1)
        if not existing:
            env["uom.uom"].create({
                "name": uom_data["name"],
                "relative_uom_id": meter.id,
                "relative_factor": uom_data["factor"],
            })

