import area


PEOPLE_PER_SQUARE_METER = 2  # numero de pessoas por metro quadrado em média
FIELD_L = 240  # em metros
FIELD_W = 45  # em metros
PEOPLE_AT_CONCERT = area.rectangle(FIELD_L, FIELD_W) // PEOPLE_PER_SQUARE_METER


print("Estão presentes no show aproximadamente", PEOPLE_AT_CONCERT, "pessoas")
