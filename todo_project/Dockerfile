# Python 3.10-u istifadə edən əsas görüntü
FROM python:3.10-slim

# Ətraf mühit dəyişənləri (Pythonda bytecode yazılmasın və tamponlama deaktiv olsun)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Layihənin iş qovluğunun yaradılması
WORKDIR /code

# requirements.txt faylını konteynerə kopyalayırıq
COPY requirements.txt /code/

# Asılılıqları quraşdırırıq
RUN pip install --no-cache-dir -r requirements.txt

# Layihə fayllarını konteynerə kopyalayırıq
COPY . /code/

# Django serverini başlatmaq üçün əmr
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
