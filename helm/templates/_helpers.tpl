{{/*
Create a unique app name
*/}}
{{- define "elementor-flask.name" -}}
{{- printf "%s" .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "elementor-flask.labels" -}}
{{ include "elementor-flask.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "elementor-flask.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
{{- end }}
