{{/*
Generate full name
*/}}
{{- define "yet-another-generator.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Get backend deployment name
*/}}
{{- define "backend.deployment.name" -}}
{{- printf "%s-%s" .Release.Name .Values.backend.name -}}
{{- end -}}

{{/*
Get backend service name
*/}}
{{- define "backend.service.name" -}}
{{- printf "%s-%s-service" .Release.Name .Values.backend.name -}}
{{- end -}}

{{/*
Get redis deployment name
*/}}
{{- define "redis.deployment.name" -}}
{{- printf "%s-%s" .Release.Name .Values.redis.name -}}
{{- end -}}

{{/*
Get redis service name
*/}}
{{- define "redis.service.name" -}}
{{- printf "%s-%s-service" .Release.Name .Values.redis.name -}}
{{- end -}}