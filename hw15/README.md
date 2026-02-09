## Домашнее задание 15

### Развернем базовый вариант с помощью helm
```
helm install release .
```
![Вариант с начальными настройками](screens/base.jpg)

### Вариант с лимитами по памяти/cpu
```
helm upgrade --install release . \
  --set backend.resources.requests.memory="512Mi" \
  --set backend.resources.limits.memory="1Gi" \
  --set backend.resources.requests.cpu="567m" \
  --set backend.resources.limits.cpu="1000m"
```
![Запуск](screens/second_1.jpg)
![Обновленные лимиты в describe pods](screens/second_2.jpg)
![Примеры запросов в сервис](screens/second_3.jpg)

### Возьмем нестандартный образ
```
helm upgrade --install release . --set redis.image.tag="7.4.7-alpine"
```
![Запуск](screens/third.jpg)