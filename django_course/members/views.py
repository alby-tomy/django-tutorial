from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Member
from .serializers import MemberSerializer


# ── DRF API Views (return JSON) ────────────────────────────────────────────────

@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def members_data(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def member_detail(request, pk):
    member = Member.objects.filter(pk=pk).first()
    if member is None:
        return Response({'detail': 'Member not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(MemberSerializer(member).data)

    if request.method in ('PUT', 'PATCH'):
        serializer = MemberSerializer(member, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    member.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# ── HTML Template Views (return rendered HTML pages) ──────────────────────────

def app_welcome(request):
    return render(request, 'welcome.html')


def members(request):
    """List all members — renders members.html."""
    all_members = Member.objects.all()
    return render(request, 'members.html', {'mymembers': all_members})


def member_detail_view(request, pk):
    """Show a single member's profile — renders details.html."""
    member = Member.objects.filter(pk=pk).first()
    if member is None:
        return redirect('members')
    return render(request, 'details.html', {'mymember': member})


def member_delete_view(request, pk):
    """Delete a member (POST only) then redirect to the list."""
    if request.method == 'POST':
        member = Member.objects.filter(pk=pk).first()
        if member:
            member.delete()
    return redirect('members')


def member_update_view(request, pk):
    """Show the edit form (GET) or save changes (POST)."""
    member = Member.objects.filter(pk=pk).first()
    if member is None:
        return redirect('members')

    if request.method == 'POST':
        member.name = request.POST.get('name', member.name)
        age = request.POST.get('age', '').strip()
        member.age = int(age) if age else None
        member.email = request.POST.get('email', member.email)
        member.contact_number = request.POST.get('contact_number', '')
        member.address = request.POST.get('address', '')
        member.social_media_url = request.POST.get('social_media_url', '')
        if 'profile_image' in request.FILES:
            member.profile_image = request.FILES['profile_image']
        member.save()
        return redirect('member_detail_view', pk=member.pk)

    return render(request, 'update.html', {'mymember': member})
