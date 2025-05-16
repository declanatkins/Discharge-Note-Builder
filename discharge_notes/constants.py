GENERATOR_INSTRUCTIONS = """
You will be given a consulation object which contatins the following fields:
{
  "patient": {
    "name": "string",
    "species": "string",
    "breed": "string",
    "gender": "string",
    "neutered": "boolean",
    "date_of_birth": "string (YYYY-MM-DD)",
    "microchip": "string | null",
    "weight": "string (e.g., '3.2 kg')"
  },
  "consultation": {
    "date": "string (YYYY-MM-DD)",
    "time": "string (HH:mm)",
    "reason": "string",
    "type": "string",
    "clinical_notes": [
      {
        "type": "string",
        "note": "string"
      }
    ],
    "treatment_items": {
      "procedures": [
        {
          "date": "string (YYYY-MM-DD)",
          "time": "string (HH:mm)",
          "name": "string",
          "code": "string",
          "quantity": "number",
          "total_price": "number",
          "currency": "string"
        }
      ],
      "medicines": [],
      "prescriptions": [],
      "foods": [],
      "supplies": []
    },
    "diagnostics": []
  }
}

From this data you will need to generate a discharge note for the patient. The discharge note should
be a set of simple instructions summarizing what happened during the consultations and what are the
next steps the patient should take.
"""
