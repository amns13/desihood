from django.contrib import admin

from .models import Artist, Song, SongArtist, Label, Language


#admin.site.register(Artist)
#admin.site.register(Song)
#admin.site.register(SongArtist)
#admin.site.register(Label)
admin.site.register(Language)


class LanguageInline(admin.TabularInline):
    model = Song.languages.through

class SongArtistInline(admin.TabularInline):
    model = SongArtist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    # first_name, last_name will be shown on same line.
    fieldsets = (
        (None, {
            'fields': ('name', ('first_name', 'last_name'), 'date_of_birth')
        }),
        ('Links', {
            'classes': ('wide',),
            'fields': ('youtube_url', 'spotify_url'),
            'description': "<b>Youtube and Spotify pages.</b>"
        }),
    )

    list_display = ('name', 'first_name', 'last_name', 'label')
    list_filter = ('name', 'label')
    search_fields = ['name', 'label__name']
    show_full_result_count = True

    inlines = [
        SongArtistInline,
    ]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    exclude = ('languages',)
    inlines = [
        LanguageInline,
        SongArtistInline,
    ]

    list_display = ('title',)
    list_filter = ('languages',)
    search_fields = ('title', 'artists__name')


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass