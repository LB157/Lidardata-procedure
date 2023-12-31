// Generated by gencpp from file pandar_msgs/PandarPacket.msg
// DO NOT EDIT!


#ifndef PANDAR_MSGS_MESSAGE_PANDARPACKET_H
#define PANDAR_MSGS_MESSAGE_PANDARPACKET_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pandar_msgs
{
template <class ContainerAllocator>
struct PandarPacket_
{
  typedef PandarPacket_<ContainerAllocator> Type;

  PandarPacket_()
    : stamp()
    , data()
    , size(0)  {
    }
  PandarPacket_(const ContainerAllocator& _alloc)
    : stamp()
    , data(_alloc)
    , size(0)  {
  (void)_alloc;
    }



   typedef ros::Time _stamp_type;
  _stamp_type stamp;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _data_type;
  _data_type data;

   typedef uint32_t _size_type;
  _size_type size;





  typedef boost::shared_ptr< ::pandar_msgs::PandarPacket_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pandar_msgs::PandarPacket_<ContainerAllocator> const> ConstPtr;

}; // struct PandarPacket_

typedef ::pandar_msgs::PandarPacket_<std::allocator<void> > PandarPacket;

typedef boost::shared_ptr< ::pandar_msgs::PandarPacket > PandarPacketPtr;
typedef boost::shared_ptr< ::pandar_msgs::PandarPacket const> PandarPacketConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pandar_msgs::PandarPacket_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pandar_msgs::PandarPacket_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pandar_msgs::PandarPacket_<ContainerAllocator1> & lhs, const ::pandar_msgs::PandarPacket_<ContainerAllocator2> & rhs)
{
  return lhs.stamp == rhs.stamp &&
    lhs.data == rhs.data &&
    lhs.size == rhs.size;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pandar_msgs::PandarPacket_<ContainerAllocator1> & lhs, const ::pandar_msgs::PandarPacket_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pandar_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pandar_msgs::PandarPacket_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pandar_msgs::PandarPacket_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pandar_msgs::PandarPacket_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c29f0f7365a75504f5f0008b5913cb94";
  }

  static const char* value(const ::pandar_msgs::PandarPacket_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc29f0f7365a75504ULL;
  static const uint64_t static_value2 = 0xf5f0008b5913cb94ULL;
};

template<class ContainerAllocator>
struct DataType< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pandar_msgs/PandarPacket";
  }

  static const char* value(const ::pandar_msgs::PandarPacket_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# field		size(byte)\n"
"# SOB 		2\n"
"# angle		2\n"
"# measure	5\n"
"# block		SOB + angle + measure * 40\n"
"# timestamp	4\n"
"# factory	2\n"
"# reserve	8\n"
"# rpm		2\n"
"# tail		timestamp + factory + reserve + rpm\n"
"# packet	block * 6 + tail\n"
"\n"
"time stamp\n"
"uint8[] data\n"
"uint32 size\n"
;
  }

  static const char* value(const ::pandar_msgs::PandarPacket_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stamp);
      stream.next(m.data);
      stream.next(m.size);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PandarPacket_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pandar_msgs::PandarPacket_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pandar_msgs::PandarPacket_<ContainerAllocator>& v)
  {
    s << indent << "stamp: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.stamp);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.data[i]);
    }
    s << indent << "size: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.size);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PANDAR_MSGS_MESSAGE_PANDARPACKET_H
