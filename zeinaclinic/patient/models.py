from django.db import models

class Patient(models.Model):
    # Basic identity
    cognome = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    numero_cartella = models.CharField("N° cartella", max_length=50, blank=True)
    data_nascita = models.DateField(null=True, blank=True)
    telefono = models.CharField("N° di telefono", max_length=50, blank=True)
    nazionalita = models.CharField(max_length=100, blank=True)
    data_arrivo_italia = models.DateField(null=True, blank=True)
    prima_visita = models.DateField(null=True, blank=True)

    # Profession
    professione_origine = models.CharField(max_length=200, blank=True)
    professione_italia = models.CharField(max_length=200, blank=True)

    # Health system codes
    stp = models.CharField(max_length=100, blank=True)
    esenzioni = models.CharField(max_length=200, blank=True)

    # Migration reason
    motivo_migrazione = models.CharField(
        max_length=100,
        choices=[
            ("Lavoro", "Lavoro"),
            ("Guerra", "Guerra"),
            ("Politico", "Politico"),
            ("Altro", "Altro"),
        ],
        blank=True
    )

    # Rete sociale
    ha_famiglia_in_patria = models.BooleanField(default=False)
    ha_famiglia_in_italia = models.BooleanField(default=False)
    ha_parenti_in_italia = models.BooleanField(default=False)
    ha_amici_in_italia = models.BooleanField(default=False)

    # Education
    titolo_studio = models.CharField(
        max_length=50,
        choices=[
            ("Elementari", "Elementari"),
            ("Medie", "Medie"),
            ("Superiori", "Superiori"),
            ("Università", "Università"),
        ],
        blank=True
    )

    # Lifestyle
    stile_vita = models.CharField(
        max_length=50,
        choices=[
            ("Regolare", "Regolare con requisiti minimi"),
            ("Stabile", "Stabile senza requisiti minimi"),
            ("Precario", "Precario"),
            ("Comunita", "Comunità/dormitori"),
        ],
        blank=True
    )

    # Occupation
    occupazione = models.CharField(
        max_length=50,
        choices=[
            ("Stabile", "Stabile"),
            ("Occasionale", "Occasionale"),
            ("Disoccupato", "Disoccupato"),
        ],
        blank=True
    )

    # Language skills
    conoscenza_italiano = models.CharField(
        max_length=50,
        choices=[
            ("Scarsa", "Scarsa (necessita traduzione)"),
            ("Sufficiente", "Sufficiente"),
            ("Ottima", "Ottima"),
        ],
        blank=True
    )
    seconda_lingua = models.CharField(max_length=100, blank=True)

    # --- NEW: Anamnesi familiare (checkboxes)
    fam_ipertensione = models.BooleanField(default=False)
    fam_diabete = models.BooleanField(default=False)
    fam_epilessia = models.BooleanField(default=False)
    fam_infarto = models.BooleanField(default=False)
    fam_neoplasia = models.BooleanField(default=False)
    fam_mal_immunologiche = models.BooleanField(default=False)
    fam_stroke = models.BooleanField(default=False)
    fam_tbc_hiv_hbv_hcv = models.BooleanField(default=False)
    fam_mal_renali = models.BooleanField(default=False)
    fam_altro = models.CharField(max_length=200, blank=True)

    # --- NEW: Anamnesi patologica remota (checkboxes)
    rem_ipertensione = models.BooleanField(default=False)
    rem_diabete = models.BooleanField(default=False)
    rem_tbc = models.BooleanField(default=False)
    rem_mal_immunologiche = models.BooleanField(default=False)
    rem_infarto = models.BooleanField(default=False)
    rem_neoplasia = models.BooleanField(default=False)
    rem_hiv = models.BooleanField(default=False)
    rem_mal_renali = models.BooleanField(default=False)
    rem_stroke = models.BooleanField(default=False)
    rem_epilessia = models.BooleanField(default=False)
    rem_hbv_hcv = models.BooleanField(default=False)

    # NEW: Allergie
    allergie = models.TextField(blank=True)

    # Habits (already present)
    fumo = models.BooleanField(default=False)
    alcool = models.BooleanField(default=False)
    droghe = models.BooleanField("Sostanze stupefacenti", default=False)

    # Current therapy
    terapia = models.TextField(blank=True)
    farmaci_costosi = models.CharField("Farmaci particolari/costosi", max_length=200, blank=True)

    # Reason for visit and physical exam
    motivo_visita = models.TextField("Anamnesi patologica prossima/motivo della visita", blank=True)
    esame_obiettivo = models.TextField(blank=True)
    programma = models.TextField(blank=True)

    # Clinical notes
    diario_clinico = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cognome}, {self.nome} ({self.data_nascita})"
