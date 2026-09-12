from django.db import models
from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    semester = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f"Semester {self.semester}"


class Student(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    BLOOD_GROUP = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    CATEGORY = [
        ("General", "General"),
        ("OBC", "OBC"),
        ("SC", "SC"),
        ("ST", "ST"),
        ("EWS", "EWS"),
    ]

    STATUS = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    admission_number = models.CharField(max_length=20, unique=True)
    roll_number = models.CharField(max_length=20, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    dob = models.DateField()

    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP,
        blank=True,
    )

    aadhaar_number = models.CharField(
        max_length=12,
        blank=True,
    )

    mobile = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    address = models.TextField()

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.SET_NULL,
        null=True,
    )

    session = models.CharField(max_length=20)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY,
    )

    religion = models.CharField(max_length=50)

    nationality = models.CharField(max_length=50)

    guardian_name = models.CharField(max_length=100)

    guardian_mobile = models.CharField(max_length=15)

    guardian_relation = models.CharField(max_length=50)

    admission_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Active",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.roll_number} - {self.first_name} {self.last_name}"